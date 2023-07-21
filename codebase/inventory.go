package inventory

import (
	"fmt"
)

type Entry struct {
	product_id string
	model      string
	ram        int
	storage    int
	price      int
	receipt_id string
}

func promt_new(Entry) {
	new_entry := Entry{product_id: "test"}
	fmt.Println(new_entry.product_id)
}
func main() {
	new_entry := Entry{product_id: "test"}
	fmt.Println(new_entry.product_id)
}
