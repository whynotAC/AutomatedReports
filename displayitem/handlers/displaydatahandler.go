package handlers

import (
	"encoding/json"
	"html/template"
	"io/ioutil"
	"log"
	"net/http"
)

type yeardatastruct struct {
	Sum   int64            `json:"sum"`
	Month map[string]int64 `json:"month"`
}

type DisplayDataStruct struct {
	YearData map[string]yeardatastruct
}

func DisplayDataHandler(w http.ResponseWriter, r *http.Request) {
	var b []byte
	var readjson DisplayDataStruct
	wr, err := template.ParseFiles("./templatesfile/base.html", "./templatesfile/pagehtml/displaydatabyyear.html")
	if err != nil {
		log.Println("Enter1")
		goto Error
	} else {
		b, err = ioutil.ReadFile("./data/Statistics.json")
		if err != nil {
			log.Println("Enter2")
			goto Error
		} else {
			if err = json.Unmarshal(b, &readjson.YearData); err != nil {
				log.Println("Enter3")
				goto Error
			} else {
				data := struct {
					Title      string
					TitleText  string
					LegendText []string
					Showjson   DisplayDataStruct
				}{
					Title:      "获取内容可视化",
					TitleText:  "Echarts表示每年文章量",
					LegendText: []string{"文章数量"},
					Showjson:   readjson,
				}
				wr.ExecuteTemplate(w, wr.Name(), data)
				goto NoError
			}
		}
	}
Error:
	wr, _ = template.ParseFiles("./templatesfile/error.html")
	wr.Execute(w, nil)
NoError:
}

func DisplayDataByPic(w http.ResponseWriter, r *http.Request) {
	wr, _ := template.ParseFiles("./templatesfile/base.html", "./templatesfile/pagehtml/displaybypic.html")
	data := struct {
		Title string
	}{
		Title: "获取内容可视化",
	}
	wr.ExecuteTemplate(w, wr.Name(), data)
}
