from alaraby import alaraby
from aljazeera import aljazeera
from washington_post import wp
from box_css import box, footer

from flask import *

app = Flask(__name__)

@app.route("/")
def home():
    return f'''
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>Middle East News | Free Palestine</title>
  </head>
  <body>


<nav class="navbar navbar-light bg-light">
  <a class="navbar-brand" href="#">
    <img src="https://cdn.countryflags.com/thumbs/palestine/flag-round-250.png" width="30" height="30" class="d-inline-block align-top" alt="">
    Middle East ∙ News
  </a>
</nav>

{box}

<div class="lists">
  <div class="list-container">
    <h2>&nbsp;AlJazeera <sub>(<a href="https://www.aljazeera.com" style="color: blue">aljazeera.com</a>)</sub></h2>
    <ul>
      <li>
        <i><a href="{aljazeera(0)[1]}" style="color: #640066">{aljazeera(0)[0]}</a></i>
      </li>
      <li>
        <i><a href="{aljazeera(1)[1]}" style="color: #640066">{aljazeera(1)[0]}</a></i>
      </li>
      <li>
        <i><a href="{aljazeera2(0)[1]}" style="color: #640066">{aljazeera2(0)[0]}</a></i>
      </li>
      <li>
        <i><a href="{aljazeera2(1)[1]}" style="color: #640066">{aljazeera2(1)[0]}</a></i>
      </li>
      <li>
        <i><a href="{aljazeera2(2)[1]}" style="color: #640066">{aljazeera2(2)[0]}</a></i>
      </li>
      <li>
      <i><a href="{aljazeera2(3)[1]}" style="color: #640066">{aljazeera2(3)[0]}</a></i>
      </li>
      <li>
      <i><a href="{aljazeera2(4)[1]}" style="color: #640066">{aljazeera2(4)[0]}</a></i>
      </li>
      <li>
      <i><a href="{aljazeera2(5)[1]}" style="color: #640066">{aljazeera2(5)[0]}</a></i>
      </li>
      <li>
      <i><a href="{aljazeera2(6)[1]}" style="color: #640066">{aljazeera2(6)[0]}</a></i>
      </li>
      <li>
      <i><a href="{aljazeera2(7)[1]}" style="color: #640066">{aljazeera2(7)[0]}</a></i>
      </li>
    </ul>
  </div>
  <div class="list-container">
    <h2>&nbsp;Washington Post <sub>(<a href="https://www.washingtonpost.com/world/middle-east/" style="color: blue">washingtonpost.com</a>)</sub></h2>
    <ul>
      <li>
      <i><a href="{wp(0)[1]}" style="color: #640066">{wp(0)[0]}</a></i>
      </li>
      <li>
        <i><a href="{wp(1)[1]}" style="color: #640066">{wp(1)[0]}</a></i>
      </li>
      <li>
        <i><a href="{wp(2)[1]}" style="color: #640066">{wp(2)[0]}</a></i>
      </li>
      <li>
        <i><a href="{wp(3)[1]}" style="color: #640066">{wp(3)[0]}</a></i>
      </li>
      <li>
        <i><a href="{wp(4)[1]}" style="color: #640066">{wp(4)[0]}</a></i>
      </li>
      <li>
        <i><a href="{wp(5)[1]}" style="color: #640066">{wp(5)[0]}</a></i>
      </li>
      <li>
        <i><a href="{wp(6)[1]}" style="color: #640066">{wp(6)[0]}</a></i>
      </li>
      <li>
        <i><a href="{wp(7)[1]}" style="color: #640066">{wp(7)[0]}</a></i>
      </li>
      <li>
        <i><a href="{wp(8)[1]}" style="color: #640066">{wp(8)[0]}</a></i>
      </li>
      <li>
        <i><a href="{wp(9)[1]}" style="color: #640066">{wp(9)[0]}</a></i>
      </li>
      <li>
        <i><a href="{wp(10)[1]}" style="color: #640066">{wp(10)[0]}</a></i>
      </li>
    </ul>
  </div>
  <div class="list-container">
    <h2>&nbsp;Alaraby <sub>(<a href="https://www.english.alaraby.co.uk/" style="color: blue">alaraby.com</a>)</sub></h2>
    <ul>
      <li>
      <i><a href="{alaraby(0)[1]}" style="color: #640066">{alaraby(0)[0]}</a></i>
      </li>
      <li>
        <i><a href="{alaraby(1)[1]}" style="color: #640066">{alaraby(1)[0]}</a></i>
      </li>
      <li>
        <i><a href="{alaraby(2)[1]}" style="color: #640066">{alaraby(2)[0]}</a></i>
      </li>
      <li>
        <i><a href="{alaraby(3)[1]}" style="color: #640066">{alaraby(3)[0]}</a></i>
      </li>
      <li>
        <i><a href="{alaraby(4)[1]}" style="color: #640066">{wp(4)[0]}</a></i>
      </li>
      <li>
        <i><a href="{alaraby(5)[1]}" style="color: #640066">{alaraby(5)[0]}</a></i>
      </li>
      <li>
        <i><a href="{alaraby(6)[1]}" style="color: #640066">{alaraby(6)[0]}</a></i>
      </li>
      <li>
        <i><a href="{alaraby(7)[1]}" style="color: #640066">{alaraby(7)[0]}</a></i>
      </li>
      <li>
        <i><a href="{alaraby(8)[1]}" style="color: #640066">{alaraby(8)[0]}</a></i>
      </li>
      <li>
        <i><a href="{alaraby(9)[1]}" style="color: #640066">{alaraby(9)[0]}</a></i>
      </li>
      <li>
        <i><a href="{alaraby(10)[1]}" style="color: #640066">{alaraby(10)[0]}</a></i>
      </li>
    </ul>
  </div>
  </lists>

    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>

    {footer}
    <div class="footer">
    <p><b>Copyright (C) | 2021 | Ram9 | All Rights Reserved</b></p>
    </div>

  </body>
</html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
