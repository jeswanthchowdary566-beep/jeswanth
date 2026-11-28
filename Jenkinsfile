pipeline {
    agent any
 
    environment {
        APP_URL = "http://127.0.0.1:5000"
    }
 
    stages {
 
        stage('Checkout') {
            steps {
                echo 'Fetching Project from GitHub'
                checkout scm
            }
        }
 
        stage('Install Dependencies') {
            steps {
                echo 'Installing Python Dependencies'
                bat 'python -m pip install -r requirements.txt'
            }
        }
 
        stage('Start Flask Application') {
            steps {
                echo 'Starting Flask Application'
                bat 'start "FlaskApp" /B python app.py'
            }
        }
         stage('Execute API Test') {
            steps {
                echo 'Starting Flask Application'
                bat '''python -m robot tese2.robot'
            }
        }
 
        stage('Test Application') {
            steps {
                echo 'Testing Flask Application'
                bat 'python -c "import urllib.request; print(urllib.request.urlopen(\'http://127.0.0.1:5000\').status)"'
            }
        }
    }
}
