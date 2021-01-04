pipeline {
  agent any
  stages {
     stage ("Build") {
        steps {
           sh "pip install -r requirements.txt"
        }
     }
     stage ("Deploy") {
       environment {
       mycreds = credentials('cf-flask')
    }
       steps {
         sh "cf login -a https://api.cf.us10.hana.ondemand.com -u $mycreds_USR -p $mycreds_PSW"
         sh "cf push my-python-app1 -m 128M --random-route"
       }
     }
  }
}
