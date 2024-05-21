from flask import Flask
import json



def read_file_json   (filename) -> list | None:
 with open("colors.json","r") as filename:
        colors_list=json.load(filename)
        print(colors_list)
        return(colors_list)
read_file_json()

def update_file_json (filename: str, colors_list: list) -> None:
     with open(filename, "w") as file_json:
        json.dump(obj=colors_list, fp=file_json, indent=4)



