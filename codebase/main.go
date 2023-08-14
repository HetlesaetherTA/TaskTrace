package main

import (
	// "github.com/HetlesaetherTA/TaskTrace/codebase/inventory"

	"fmt"

	Filesystem "github.com/HetlesaetherTA/TaskTrace/codebase/filesystem"
)

func main() {
	path, err := Filesystem.Search("20230814142344")

	if err != nil {
		fmt.Println(err)
	}

	err = Filesystem.Delete(path)
}
