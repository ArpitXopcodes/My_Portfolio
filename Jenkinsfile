pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning GitHub repository...'
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo 'Setting up Python virtual environment...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running pytest...'
                sh '''
                    . venv/bin/activate
                    pytest test_app.py -v
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t arpit-portfolio:latest .'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh '''
                    docker stop arpit-portfolio || true
                    docker rm arpit-portfolio || true
                    docker run -d --name arpit-portfolio -p 5000:5000 arpit-portfolio:latest
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully! Application is deployed.'
        }
        failure {
            echo 'Pipeline failed. Check the logs above for errors.'
        }
    }
}
