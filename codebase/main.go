package main

import (
	// "github.com/HetlesaetherTA/TaskTrace/codebase/inventory"
	"fmt"

	"github.com/HetlesaetherTA/TaskTrace/codebase/filesystem"
)
func main() {
  // test := Inventory.Promt_new()
  // Filesystem.CreateJson(test)
  test := Filesystem.Delete("20230807145041")
  fmt.Println(test)
}

