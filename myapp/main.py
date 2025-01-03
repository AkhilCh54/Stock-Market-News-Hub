from datetime import datetime
from flask import Flask, render_template, request, url_for, redirect
import smtplib

from_address = "m16631906@gmail.com"
password = "ruhjncujreknuxbu"
to_addr = "chakhilsatyasai225@gmail.com"
#==========================================================================================================================
# Automating the Date Variable

now = datetime.now() # current date and time

year = now.strftime("%Y")     #current year
#print(f"year: {year}")

month = int(now.strftime("%m"))     #current month
#print(f"month: {month}")

current_day_minus_15 = int(now.strftime("%d")) - 15           # day set to 15 days prior to current date
#print(f"day: {current_day_minus_15}")

if current_day_minus_15<1:
    current_day_minus_15 = 30 + current_day_minus_15
    month = month - 1

DATE = f"{year}-{month}-{current_day_minus_15}"    

#===========================================================================================================================
class Post:
    def __init__(self, post_id, title, subtitle):
        self.id = post_id
        self.title = title
        self.subtitle = subtitle
#========================================================================================================================
# NEWS API  #STOCK MARKET
import requests

parameters_news = {
    'q': "STOCK MARKET",
    'from':DATE,
    'sortBy':'publishedAt',
    'language': 'en',
    'apiKey':'003dad8d7bff4974806223db9230b906',
}
news_response = requests.get(url='https://newsapi.org/v2/everything',params=parameters_news)

articles = news_response.json()['articles']
article_1_id = 1
article_1_name = articles[0]['source']['name']
article_1_title = articles[0]['title']

article_2_id = 2
article_2_name = articles[1]['source']['name']
article_2_title = articles[1]['title']

article_3_id = 3
article_3_name = articles[2]['source']['name']
article_3_title = articles[2]['title']

article_4_id = 4
article_4_name = articles[3]['source']['name']
article_4_title = articles[3]['title']

article_5_id = 5
article_5_name = articles[4]['source']['name']
article_5_title = articles[4]['title']

article_6_id = 6
article_6_name = articles[5]['source']['name']
article_6_title = articles[5]['title']

article_7_id = 7
article_7_name = articles[6]['source']['name']
article_7_title = articles[6]['title']

article_8_id = 8
article_8_name = articles[7]['source']['name']
article_8_title = articles[7]['title']

article_9_id = 9
article_9_name = articles[8]['source']['name']
article_9_title = articles[8]['title']

article_10_id = 10
article_10_name = articles[9]['source']['name']
article_10_title = articles[9]['title']

#=======================================================================================================================
#NEWS API #TESLA

tesla_parameters_news = {
    'q': "Tesla",
    'from':DATE,
    'sortBy':'publishedAt',
    'language': 'en',
    'apiKey':'003dad8d7bff4974806223db9230b906',
}
tesla_news_response = requests.get(url='https://newsapi.org/v2/everything',params=tesla_parameters_news)

tesla_articles = tesla_news_response.json()['articles']
tesla_article_1_id = 1
tesla_article_1_name = tesla_articles[0]['source']['name']
tesla_article_1_title = tesla_articles[0]['title']

tesla_article_2_id = 2
tesla_article_2_name = tesla_articles[1]['source']['name']
tesla_article_2_title = tesla_articles[1]['title']

tesla_article_3_id = 3
tesla_article_3_name = tesla_articles[2]['source']['name']
tesla_article_3_title = tesla_articles[2]['title']

tesla_article_4_id = 4
tesla_article_4_name = tesla_articles[3]['source']['name']
tesla_article_4_title = tesla_articles[3]['title']

tesla_article_5_id = 5
tesla_article_5_name = tesla_articles[4]['source']['name']
tesla_article_5_title = tesla_articles[4]['title']

#==========================================================================================================================
# NOKIA NEWS API
nokia_parameters_news = {
    'q': "nokia",
    'from':DATE,
    'sortBy':'publishedAt',
    'language': 'en',
    'apiKey':'003dad8d7bff4974806223db9230b906',
}
nokia_news_response = requests.get(url='https://newsapi.org/v2/everything',params=nokia_parameters_news)

nokia_articles = nokia_news_response.json()['articles']
nokia_article_1_id = 1
nokia_article_1_name = nokia_articles[0]['source']['name']
nokia_article_1_title = nokia_articles[0]['title']

nokia_article_2_id = 2
nokia_article_2_name = nokia_articles[1]['source']['name']
nokia_article_2_title = nokia_articles[1]['title']

nokia_article_3_id = 3
nokia_article_3_name = nokia_articles[2]['source']['name']
nokia_article_3_title = nokia_articles[2]['title']

nokia_article_4_id = 4
nokia_article_4_name = nokia_articles[3]['source']['name']
nokia_article_4_title = nokia_articles[3]['title']

nokia_article_5_id = 5
nokia_article_5_name = nokia_articles[4]['source']['name']
nokia_article_5_title = nokia_articles[4]['title']
#============================================================================================================
# google NEWS API
google_parameters_news = {
    'q': "Alphabet Inc Class A",
    'from':DATE,
    'sortBy':'publishedAt',
    'language': 'en',
    'apiKey':'003dad8d7bff4974806223db9230b906',
}
google_news_response = requests.get(url='https://newsapi.org/v2/everything',params=google_parameters_news)

google_articles = google_news_response.json()['articles']
google_article_1_id = 1
google_article_1_name = google_articles[0]['source']['name']
google_article_1_title = google_articles[0]['title']

google_article_2_id = 2
google_article_2_name = google_articles[1]['source']['name']
google_article_2_title = google_articles[1]['title']

google_article_3_id = 3
google_article_3_name = google_articles[2]['source']['name']
google_article_3_title = google_articles[2]['title']

google_article_4_id = 4
google_article_4_name = google_articles[3]['source']['name']
google_article_4_title = google_articles[3]['title']

google_article_5_id = 5
google_article_5_name = google_articles[4]['source']['name']
google_article_5_title = google_articles[4]['title']
#============================================================================================================
# intel NEWS API
intel_parameters_news = {
    'q': "intel",
    'from':DATE,
    'sortBy':'publishedAt',
    'language': 'en',
    'apiKey':'003dad8d7bff4974806223db9230b906',
}
intel_news_response = requests.get(url='https://newsapi.org/v2/everything',params=intel_parameters_news)

intel_articles = intel_news_response.json()['articles']
intel_article_1_id = 1
intel_article_1_name = intel_articles[0]['source']['name']
intel_article_1_title = intel_articles[0]['title']

intel_article_2_id = 2
intel_article_2_name = intel_articles[1]['source']['name']
intel_article_2_title = intel_articles[1]['title']

intel_article_3_id = 3
intel_article_3_name = intel_articles[2]['source']['name']
intel_article_3_title = intel_articles[2]['title']

intel_article_4_id = 4
intel_article_4_name = intel_articles[3]['source']['name']
intel_article_4_title = intel_articles[3]['title']

intel_article_5_id = 5
intel_article_5_name = intel_articles[4]['source']['name']
intel_article_5_title = intel_articles[4]['title']
#============================================================================================================
# amazon NEWS API
amazon_parameters_news = {
    'q': "amazon",
    'from':DATE,
    'sortBy':'publishedAt',
    'language': 'en',
    'apiKey':'003dad8d7bff4974806223db9230b906',
}
amazon_news_response = requests.get(url='https://newsapi.org/v2/everything',params=amazon_parameters_news)

amazon_articles = amazon_news_response.json()['articles']
amazon_article_1_id = 1
amazon_article_1_name = amazon_articles[0]['source']['name']
amazon_article_1_title = amazon_articles[0]['title']

amazon_article_2_id = 2
amazon_article_2_name = amazon_articles[1]['source']['name']
amazon_article_2_title = amazon_articles[1]['title']

amazon_article_3_id = 3
amazon_article_3_name = amazon_articles[2]['source']['name']
amazon_article_3_title = amazon_articles[2]['title']

amazon_article_4_id = 4
amazon_article_4_name = amazon_articles[3]['source']['name']
amazon_article_4_title = amazon_articles[3]['title']

amazon_article_5_id = 5
amazon_article_5_name = amazon_articles[4]['source']['name']
amazon_article_5_title = amazon_articles[4]['title']

#===============================================================================================================
def create_app():
    # STOCK MARKET POST OBJECTS
    post_objects = []
    post_obj1 = Post(article_1_id, article_1_title, article_1_name)
    post_obj2 = Post(article_2_id, article_2_title, article_2_name)
    post_obj3 = Post(article_3_id, article_3_title, article_3_name)
    post_obj4 = Post(article_4_id, article_4_title, article_4_name)
    post_obj5 = Post(article_5_id, article_5_title, article_5_name)
    post_obj6 = Post(article_6_id, article_6_title, article_6_name)
    post_obj7 = Post(article_7_id, article_7_title, article_7_name)
    post_obj8 = Post(article_8_id, article_8_title, article_8_name)
    post_obj9 = Post(article_9_id, article_9_title, article_9_name)
    post_obj10 = Post(article_10_id, article_10_title, article_10_name)
    post_objects.append(post_obj1)
    post_objects.append(post_obj2)
    post_objects.append(post_obj3)
    post_objects.append(post_obj4)
    post_objects.append(post_obj5)
    post_objects.append(post_obj6)
    post_objects.append(post_obj7)
    post_objects.append(post_obj8)
    post_objects.append(post_obj9)
    post_objects.append(post_obj10)
    #==============================================================================================
    # TESLA POST OBJECTS
    tesla_post_objects = []
    teslapost_obj1 = Post(tesla_article_1_id, tesla_article_1_title, tesla_article_1_name)
    teslapost_obj2 = Post(tesla_article_2_id, tesla_article_2_title, tesla_article_2_name)
    teslapost_obj3 = Post(tesla_article_3_id, tesla_article_3_title, tesla_article_3_name)
    teslapost_obj4 = Post(tesla_article_4_id, tesla_article_4_title, tesla_article_4_name)
    teslapost_obj5 = Post(tesla_article_5_id, tesla_article_5_title, tesla_article_5_name)
    tesla_post_objects.append(teslapost_obj1)
    tesla_post_objects.append(teslapost_obj2)
    tesla_post_objects.append(teslapost_obj3)
    tesla_post_objects.append(teslapost_obj4)
    tesla_post_objects.append(teslapost_obj5)
    #==================================================================================================
    # NOKIA POST OBJECTS
    nokia_post_objects = []
    nokiapost_obj1 = Post(nokia_article_1_id, nokia_article_1_title, nokia_article_1_name)
    nokiapost_obj2 = Post(nokia_article_2_id, nokia_article_2_title, nokia_article_2_name)
    nokiapost_obj3 = Post(nokia_article_3_id, nokia_article_3_title, nokia_article_3_name)
    nokiapost_obj4 = Post(nokia_article_4_id, nokia_article_4_title, nokia_article_4_name)
    nokiapost_obj5 = Post(nokia_article_5_id, nokia_article_5_title, nokia_article_5_name)
    nokia_post_objects.append(nokiapost_obj1)
    nokia_post_objects.append(nokiapost_obj2)
    nokia_post_objects.append(nokiapost_obj3)
    nokia_post_objects.append(nokiapost_obj4)
    nokia_post_objects.append(nokiapost_obj5)
    #===================================================================================================
    # google POST OBJECTS
    google_post_objects = []
    googlepost_obj1 = Post(google_article_1_id, google_article_1_title, google_article_1_name)
    googlepost_obj2 = Post(google_article_2_id, google_article_2_title, google_article_2_name)
    googlepost_obj3 = Post(google_article_3_id, google_article_3_title, google_article_3_name)
    googlepost_obj4 = Post(google_article_4_id, google_article_4_title, google_article_4_name)
    googlepost_obj5 = Post(google_article_5_id, google_article_5_title, google_article_5_name)
    google_post_objects.append(googlepost_obj1)
    google_post_objects.append(googlepost_obj2)
    google_post_objects.append(googlepost_obj3)
    google_post_objects.append(googlepost_obj4)
    google_post_objects.append(googlepost_obj5)
    #===================================================================================================
    #INTEL POST OBJECTS
    intel_post_objects = []
    intelpost_obj1 = Post(intel_article_1_id, intel_article_1_title, intel_article_1_name)
    intelpost_obj2 = Post(intel_article_2_id, intel_article_2_title, intel_article_2_name)
    intelpost_obj3 = Post(intel_article_3_id, intel_article_3_title, intel_article_3_name)
    intelpost_obj4 = Post(intel_article_4_id, intel_article_4_title, intel_article_4_name)
    intelpost_obj5 = Post(intel_article_5_id, intel_article_5_title, intel_article_5_name)
    intel_post_objects.append(intelpost_obj1)
    intel_post_objects.append(intelpost_obj2)
    intel_post_objects.append(intelpost_obj3)
    intel_post_objects.append(intelpost_obj4)
    intel_post_objects.append(intelpost_obj5)
    #=====================================================================================================
    #amazon POST OBJECTS
    amazon_post_objects = []
    amazonpost_obj1 = Post(amazon_article_1_id, amazon_article_1_title, amazon_article_1_name)
    amazonpost_obj2 = Post(amazon_article_2_id, amazon_article_2_title, amazon_article_2_name)
    amazonpost_obj3 = Post(amazon_article_3_id, amazon_article_3_title, amazon_article_3_name)
    amazonpost_obj4 = Post(amazon_article_4_id, amazon_article_4_title, amazon_article_4_name)
    amazonpost_obj5 = Post(amazon_article_5_id, amazon_article_5_title, amazon_article_5_name)
    amazon_post_objects.append(amazonpost_obj1)
    amazon_post_objects.append(amazonpost_obj2)
    amazon_post_objects.append(amazonpost_obj3)
    amazon_post_objects.append(amazonpost_obj4)
    amazon_post_objects.append(amazonpost_obj5)
    #=======================================================================================================
    current_year = datetime.now().year

    app = Flask(__name__)

    @app.route("/")
    def home():
        
        return render_template("home.html", all_posts=post_objects, year=current_year)

    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route("/contact", methods=['POST','GET'])
    def contact():
        
        return render_template("contact.html")

    @app.route("/contact/submit", methods=['POST','GET'])
    def submit_form():
        ans = "y"
        while True:
            name = request.form["name"]
            email = request.form["email"]
            phone = request.form["phone"]
            message = request.form["message"]
            connection = smtplib.SMTP("smtp.gmail.com")
            connection.starttls()
            connection.login(user=from_address, password=password)
            connection.sendmail(from_addr=from_address,
                                to_addrs=to_addr,
                                msg=f"subject:Message from Stock News Website website\n\nName : {name}\nEmail : {email}\n Phone Number : {phone}\nMessage : {message}")
            return "Form Submitted Successfully"
        return redirect(url_for("home"))
    
    #TESLA STOCK ROUTE
    @app.route("/stocks/tesla")
    def tesla():
        return render_template("tesla.html", all_posts=tesla_post_objects, year=current_year)
    
    #NOKIA STOCK ROUTE
    @app.route("/stocks/nokia")
    def nokia():
        return render_template("nokia.html", all_posts=nokia_post_objects, year=current_year)
    
    #GOOGLE STOCK ROUTE
    @app.route("/stocks/google")
    def google():
        return render_template("google.html", all_posts=google_post_objects, year=current_year)
    
    #INTEL STOCK ROUTE
    @app.route("/stocks/intel")
    def intel():
        return render_template("intel.html", all_posts=intel_post_objects, year=current_year)
    
    #AMAZON STOCK ROUTE
    @app.route("/stocks/amazon")
    def amazon():
        return render_template("amazon.html", all_posts=amazon_post_objects, year=current_year)
    #==================================================================================================================

    #=================================================================================================

    return app
