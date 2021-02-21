from flask import Flask, request, jsonify
from mysql.connector import connect, Error
import json
from Sentiment import findSentiment
import pymysql

#Method to connect application with MySQL Database
def connectDb():
    try:
        myDatabase = connect(
            host="localhost",
            user="root",
            password="root",
            database="sampledb"
        )
        return myDatabase
    except Error as error:
        print(f"Connection Error: {error}")
        return False


#Method to add a feedback
def add():
    myConnection = connectDb()
    print(f"Connection Status: {myConnection}")

    #If connection to database fails
    if myConnection is False:
        return jsonify({
            "error": "Connection failed"
        })
    else:
        try:
            myCursor = myConnection.cursor()

            query = ("INSERT INTO details "
               "(name, phone, email, review, feedback) "
               "VALUES (%s, %s, %s, %s, %s)")

            
            name = request.form.get("name")
            phone = request.form.get("phone")
            email = request.form.get("email")
            review = request.form.get("review")
            sentiment = findSentiment(review)

            queryData = (name, phone, email, review, sentiment)

            myCursor.execute(query, queryData)
            myConnection.commit()
            
            return "added"

        except Exception as error:
            print(error)
            return jsonify({
                "error": error
            })
        finally:
            myCursor.close()
            myConnection.close()


#Method to retrieve all feedbacks
def fetch():
    myConnection = connectDb()
    print(f"Connection Status: {myConnection}")

    #If connection to database fails
    if myConnection is False:
        return jsonify({
            "error": "Connection failed"
        })
    else:
        try:
            myCursor = myConnection.cursor(pymysql.cursors.DictCursor)
            query = "SELECT * FROM details"
            myCursor.execute(query)
            rows = myCursor.fetchall()
            response = rows
            # feedback = []
            # for i in myCursor:
            #     feedback.append(i)
                
            # return jsonify({
            #     "result": feedback
            # })

            return response

        except Exception as error:
            print(error)
            return jsonify({
                "error": error
            })
        finally:
            myCursor.close()
            myConnection.close()



