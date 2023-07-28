package Filesystem

import (
	"fmt"
	"reflect"
  "encoding/json"
  "io/ioutil"
)

func CreateJson(object interface{}) {
  val := reflect.ValueOf(object)

  if val.Kind() != reflect.Struct {
    fmt.Println("Invalid type passed as a parameter.")
    return
  }

  path := val.FieldByName("Path")
  
  jsonData, err := json.Marshal(object)
  if err != nil {
    fmt.Println("Error marshaling struct to JSON:", err)
  }
  
  err = ioutil.WriteFile(path.String(), jsonData, 0644)
  if err != nil {
    fmt.Println("Error writing JSON data to file:", err)
    return
  }
}
