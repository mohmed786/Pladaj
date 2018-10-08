#Shopify App Souce Code

from flask import Flask, render_template, request, redirect, Response, session
from config import Config as cfg
#from urllib import request, parse
#import http.client
import json
import requests


app = Flask(__name__, template_folder="templates")
app.debug = True
app.secret_key = cfg.SECRET_KEY


@app.route('/payment', methods=["GET","POST"])

def payment():

#   resultx = get_method()
#   resulty = get_method2()
    headers = {
                 "X-Shopify-Access-Token": session["access_token"],
                  "Accept": "application/json",
                  "Content-Type": "application/json" }

    payload = { "recurring_application_charge":
    {

                "name": "App charge",
                "price": 0.99,
                "return_url": "https://www.nmf786.ga/main.html"

}
               }

    #json_data = parse.urlencode(script_tag).encode('utf8')
    endpoint = "/admin/recurring_application_charges.json"

    url = "https://{0}{1}".format(session['shop'],endpoint)
    #url = "https://{0}{1}".format( session['shop'] , endpoint)
    #json1 = json.dumps(script_tag)


    req = requests.post(url , json = payload, headers = headers)



    resp = json.loads(req.text)

    print (req.status_code, resp)
    session['id'] = resp['recurring_application_charge']['id']
    session['name'] = resp['recurring_application_charge']["name"]
    session['api_client_id'] = resp['recurring_application_charge']["api_client_id"]
    session['price'] = resp['recurring_application_charge']["price"]
    session['return_url'] = resp['recurring_application_charge']["return_url"]
    session['created_at'] = resp['recurring_application_charge']["created_at"]
    session['updated_at'] = resp['recurring_application_charge']["updated_at"]
    session['decorated_return_url'] = resp['recurring_application_charge']["decorated_return_url"]
    session['confirmation_url'] = resp['recurring_application_charge']["confirmation_url"]


    if req.status_code == 201:
            return redirect(session['confirmation_url'])
    else:
            return render_template("error.html", scr = resp.content)






@app.route('/charge_finder', methods=["GET"])

def charge_finder():

#   resultx = get_method()
#   resulty = get_method2()
    headers = {
                 "X-Shopify-Access-Token": session["access_token"],
                  "Content-Type": "application/json" }




    endpoint = "/admin/recurring_application_charges/{0}.json".format(session['id'])

    url = "https://{0}{1}".format(session['shop'],endpoint)



    req = requests.get(url , headers = headers)

    print (req.status_code, req.content)

    respec = json.loads(req.text)
    var = respec['recurring_application_charge']['status']

    if req.status_code == 200:
        if var == "accepted":
            return redirect("/charge")
        else: return render_template("webhooks.html")
    else:
        return render_template("error1.html")


@app.route('/charge', methods=["GET","POST"])

def charge_():

#   resultx = get_method()
#   resulty = get_method2()
    headers = {
                 "X-Shopify-Access-Token": session["access_token"],
                  "Accept": "application/json",
                  "Content-Type": "application/json" }

    payload = { "recurring_application_charge":
    {
                "id" : session['id'],
                "name" : session['name'],
                "api_client_id" : session['api_client_id'],
                "price" : session['price'],
                "status" : "accepted",
                "billing_on" : "null",
                "created_at" : session["created_at"],
                "updated_at" : session["updated_at"],
                "activated_on" : "null",
                "trial_ends_on" : "null",
                "cancelled_on" : "null",
                "decorated_return_url" : session["decorated_return_url"]

}
               }

    #json_data = parse.urlencode(script_tag).encode('utf8')
    endpoint = "/admin/recurring_application_charges/{0}/activate.json".format(session['id'])

    url = "https://{0}{1}".format(session['shop'],endpoint)
    #url = "https://{0}{1}".format( session['shop'] , endpoint)
    #json1 = json.dumps(script_tag)


    req = requests.post(url , json = payload, headers = headers)

    print (req.status_code, req.content)

    resp = json.loads(req.text)



    if req.status_code == 200:
            return redirect("/script")
    else:
            return render_template("error.html")



@app.route('/curr_script', methods = ["GET"])

def script_authenticate():

      headers= {
          "X-Shopify-Access-Token": session.get("access_token"),
          "Content-Type": "application/json"
      }
      endpoint = "/admin/script_tags.json"
      response = requests.get("https://{0}{1}".format(session.get("shop"),
                                                      endpoint), headers=headers)
      print(response.status_code)

      if response.status_code == 200:
              scripts =  json.loads(response.text)
              print(scripts)

              return render_template('products.html',scr=scripts)

      else:
              return render_template('error1.html')



@app.route('/script', methods=["GET","POST"])

def script_auth():

#   resultx = get_method()
#   resulty = get_method2()
    headers = {
                 "X-Shopify-Access-Token": session["access_token"],
                  "Accept": "application/json",
                  "Content-Type": "application/json" }

    payload = { "script_tag": {
              "src": "https://www.nmf786.ga/rightclick.js",
              "event": "onload"
                              }
               }

    #json_data = parse.urlencode(script_tag).encode('utf8')
    endpoint = "/admin/script_tags.json"

    url = "https://{0}{1}".format(session['shop'],endpoint)
    #url = "https://{0}{1}".format( session['shop'] , endpoint)
    #json1 = json.dumps(script_tag)


    req = requests.post(url , json = payload, headers = headers)

    print (req.status_code, req.content)

    if req.status_code == 201:
            return render_template("thankyou.html", scr = req.content)
    else:
            return render_template("error.html", scr = req.content)

    #r = requests.post(""https://{0}{1}".format( session.get("shop") , endpoint", data=payload)
    #req = request.Request(url,data =json_data , method = 'POST' , headers = {
                                                                        #    "X-Shopify-Access-Token": session.get("access_token"),
                                                                        #                    "Content-Type": "application/json" })
    #resp = request.urlopen(req)
    #if resp.status_code == 201:
    #    return render_template('products.html',scr="Hola Amigo!")
    #else:
    #    return render_template('error.html')
    #conn.request('POST','/v3/call_api' , params , headers)
    #resp = conn.getresponse()
    #if resp.status_code == 201:
    #req = urllib.request.Request("https://{0}{1}".format( session.get("shop") , endpoint) , data=params , headers=headers)
    #response = urllib.request.urlopen(req)
    #if request.method == "POST"
     #response = requests.post(url="https://{0}{1}".format( session.get("shop") , endpoint) , json = script_tag , headers=headers)


#def get_method():
#        if request.method == "GET":
#            x = session.get("access_token")
#            return x


#def get_method2():
#        if request.method == "GET":
#            y =  session.get("shop")
#            return y

@app.route('/install', methods=['GET'])
def install():

    if request.args.get('shop'):
        shop = request.args.get('shop')
    else:
        return Response(response="Error:parameter shop not found", status=500)

    auth_url = "https://{0}/admin/oauth/authorize?client_id={1}&scope={2}&redirect_uri={3}".format(
        shop, cfg.SHOPIFY_CONFIG["API_KEY"], cfg.SHOPIFY_CONFIG["SCOPE"],
        cfg.SHOPIFY_CONFIG["REDIRECT_URI"]
    )
    print("Debug - auth URL: ", auth_url)
    return redirect(auth_url)


@app.route('/connect', methods=['GET'])
def connect():
    if request.args.get("shop"):
        params = {
            "client_id": cfg.SHOPIFY_CONFIG["API_KEY"],
            "client_secret": cfg.SHOPIFY_CONFIG["API_SECRET"],
            "code": request.args.get("code")
        }
        resp = requests.post(
            "https://{0}/admin/oauth/access_token".format(
                request.args.get("shop")
            ),
            data=params
        )

        if 200 == resp.status_code:
            resp_json = json.loads(resp.text)

            session['access_token'] = resp_json.get("access_token")
            session['shop'] = request.args.get("shop")

            return redirect("/payment")
        else:
            print ("Failed to get access token: "), resp.status_code, resp.text
            return render_template('error.html')




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
