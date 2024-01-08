from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import random

from markdown2 import Markdown

from . import util

def convert_to_html(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None
    else:

        return markdowner.convert(content)




def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    ui_content = convert_to_html(title)
    if ui_content == None:
        return render(request, "encyclopedia/404.html")
    else:
        return render(request,  "encyclopedia/page.html" , {
            "title": title,
            "content": ui_content                    
        })
def search(request):
    if request.method == "POST":
        entry_src = request.POST['q']
        ui_content = convert_to_html(entry_src)
        if ui_content is not None:
            return render(request,  "encyclopedia/page.html" , {
                "title": entry_src,
                "content": ui_content                     
            })
        else:
            substr = []
            for entry in util.list_entries():
                if entry_src.lower() in entry.lower():
                    substr.append(entry)
            return render(request, "encyclopedia/sugg.html",{
                "entries": substr,
                "search": True,
                "entry_src":entry_src                               
            })

def n_page(request):
    if request.method == "GET":
        return  render(request, "encyclopedia/create.html")
    else:
        name = request.POST['name']
        context = request.POST['context']
        namepresent = util.get_entry(name)
        if namepresent is not None:
            return render(request, "encyclopedia/404.html",{
                "alert": "page exists already"
            })
        else:
            util.save_entry(name, context)
            ui_content = convert_to_html(name)
            return render(request, "encyclopedia/page.html",{
                "title": name,
                "content": ui_content


            })
def edt(request):
    if request.method == 'POST':
        title = request.POST['enter_title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edt.html",{
            "title":title,
            "content": content

        })
    
def save_edt(request):
    if request.method =='POST':
        title = request.POST['name']
        content = request.POST['context']
        util.save_entry(title, content)
        ui_content = convert_to_html(title)
        return render(request, "encyclopedia/page.html",{
                "title": title,
                "content": ui_content
        })
    
def ran(request):
    all = util.list_entries()
    Rentry = random.choice(all)
    ui_content = convert_to_html(Rentry)
    return render (request, "encyclopedia/page.html",{
        "title": Rentry,
        "content":ui_content 
    })

    
        

        
  

   
           
        
        






          

    
        

    


  


    

        