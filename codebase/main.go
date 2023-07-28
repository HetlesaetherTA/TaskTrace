package main

import (
	"github.com/HetlesaetherTA/TaskTrace/codebase/inventory"
  "github.com/HetlesaetherTA/TaskTrace/codebase/filesystem"
)
func main() {
  test := Inventory.Promt_new()
  Filesystem.CreateJson(test)
}
