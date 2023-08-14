package Filesystem

import (
	"encoding/json"
	"errors"
	"fmt"
	"os"
	"path"
	"path/filepath"
	"reflect"
	"runtime"
	"strings"
)

func CreateJson(object interface{}) {
	val := reflect.ValueOf(object)

	_, b, _, _ := runtime.Caller(0)
	d := path.Join(path.Dir(b))
	root := strings.ReplaceAll(filepath.Dir(d), "codebase", "")
	root = strings.ReplaceAll(root, "\\", "/")

	if val.Kind() != reflect.Struct {
		fmt.Println("Invalid type passed as a parameter.")
		return
	}

	path := ""
	filename := ""

	if val.Field(0).Kind() == reflect.String {
		path = val.Field(0).String()
	}

	if val.Field(1).Kind() == reflect.String {
		filename = val.Field(1).String()
	}

	err := os.Mkdir(root+path, 0755)

	if err != nil {
		fmt.Println("Error creating dir", err)
	}

	file, err := os.Create(root + path + "/" + filename + ".json")
	if err != nil {
		fmt.Println("Error creating file", err)
		return
	}

	defer file.Close()

	encoder := json.NewEncoder(file)
	err = encoder.Encode(object)

	if err != nil {
		fmt.Println("Error encoding JSON", err)
		return
	}

	fmt.Println("Created: " + root + path + "/" + filename + ".json")
}

func Delete(path string) error {
	err := os.RemoveAll(path)

	if err != nil {
		return errors.New("ID not found")
	}

	return nil
}

func Search(id string) (string, error) {
	_, b, _, _ := runtime.Caller(0)
	d := path.Join(path.Dir(b))
	root := strings.ReplaceAll(filepath.Dir(d), "codebase", "")
	root = strings.ReplaceAll(root, "\\", "/")

	directories := []string{"files/Inventory/Available", "files/Inventory/Sold", "files/Receipts"}

	for i := 0; i < len(directories); i++ {
		dir, err := os.Open(root + directories[i])

		if err != nil {
			fmt.Println(err)
		}

		defer dir.Close()

		entries, err := dir.Readdir(-1)

		if err != nil {
			fmt.Println(err)
		}

		for _, entry := range entries {
			if entry.Name() == id {
				return root + directories[i] + "/" + id, nil
			}
		}
	}
	return "", errors.New("ID not found")
}
