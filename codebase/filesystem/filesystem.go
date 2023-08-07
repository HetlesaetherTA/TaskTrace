package Filesystem

import (
	"fmt"
	"reflect"
  "encoding/json"
  "runtime"
  "path"
  "path/filepath"
  "io/ioutil"
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

  if val.Field(0).Kind() == reflect.String {
    path = val.Field(0).String()
  }
  jsonData, err := json.Marshal(object)

  if err != nil {
    fmt.Println("Error marshaling struct to JSON:", err)
  }

  err = ioutil.WriteFile(root + path, jsonData, 0644)
  if err != nil {
    fmt.Println("Error writing JSON data to file:", err)
    return
  }
}
