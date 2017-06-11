package main

import (
	"ShowInfo/handlers"
	"log"
	"net/http"
)

func init() {
	http.HandleFunc("/v1/displaydata", handlers.DisplayDataHandler)
}

func main() {
	http.Handle("/static/", http.StripPrefix("/static/", http.FileServer(http.Dir("static"))))
	log.Println(http.ListenAndServe(":6080", nil))
}
