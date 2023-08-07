package Inventory

import (
  "fmt"
  "time"
  // "strconv"
)

type Entry struct {
	Path string
  Product_ID string
	Model string
  Ram int
  Storage int
  Price int
  Receipt_ID string
}

func Promt_new() interface{} {
  currentTime := time.Now()
  formattedTime := fmt.Sprintf("%d%02d%02d%d%d%d", currentTime.Year(), int(currentTime.Month()), currentTime.Day(), currentTime.Hour(), currentTime.Minute(), currentTime.Second())
   
  entry_buffer := Entry{
    Path: "files/Inventory/Available/" + formattedTime,
    Product_ID: formattedTime,
    Model: "",
    Ram: 0,
    Storage: 0,
    Price: 0,
    Receipt_ID: "",
  }
  
  fmt.Print("Model (Axxxx): ")
  fmt.Scanln(&entry_buffer.Model)
  fmt.Print("Ram: ")
  fmt.Scanln(&entry_buffer.Ram)
  fmt.Print("Storage: ")
  fmt.Scanln(&entry_buffer.Storage)
  fmt.Print("Purchase price: ")
  fmt.Scanln(&entry_buffer.Price)
  return entry_buffer
}

