pipeline {
    agent any

    environment {
        APP_NAME       = "python-flask-demo"
        CONTAINER_NAME = "python-flask-demo"
        APP_PORT       = "5060"
        HOST_PORT      = "5000"
        IMAGE_TAG      = "${env.BUILD_NUMBER}"
        APP_VERSION    = "v${env.BUILD_NUMBER}"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                echo "Building Docker image..."
                docker build -t ${APP_NAME}:${IMAGE_TAG} .
                docker tag ${APP_NAME}:${IMAGE_TAG} ${APP_NAME}:latest
                '''
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                echo "Stopping old container if exists..."
                docker ps -q --filter "name=${CONTAINER_NAME}" | grep -q . && docker stop ${CONTAINER_NAME} || true
                docker ps -aq --filter "name=${CONTAINER_NAME}" | grep -q . && docker rm ${CONTAINER_NAME} || true
                '''
            }
        }

        stage('Run New Container') {
            steps {
                sh '''
                echo "Running new container..."

                docker run -d \
                    --name ${CONTAINER_NAME} \
                    -p ${HOST_PORT}:${APP_PORT} \
                    --restart unless-stopped \
                    ${APP_NAME}:latest
                '''
            }
        }

        stage('Cleanup') {
            steps {
                sh '''
                echo "Cleaning unused images..."
                docker image prune -f
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Deployment Successful! Access app on port ${HOST_PORT}"
        }
        failure {
            echo "❌ Deployment Failed. Check logs."
        }
    }
}