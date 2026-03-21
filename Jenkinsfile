pipeline {
    agent { label 'jenkins-agent' }

    environment {
        APP_NAME       = "python-flask-demo"
        CONTAINER_NAME = "python-flask-demo"
        APP_PORT       = "5000"
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
                docker build -t ${APP_NAME}:${IMAGE_TAG} .
                docker tag ${APP_NAME}:${IMAGE_TAG} ${APP_NAME}:latest
                '''
            }
        }

        stage('Deploy on Agent (Docker Run)') {
            steps {
                sh '''
                set +e
                docker rm -f ${CONTAINER_NAME} >/dev/null 2>&1
                set -e

                docker run -d \
                    --name ${CONTAINER_NAME} \
                    -p ${HOST_PORT}:${APP_PORT} \
                    ${APP_NAME}:latest

                docker image prune -f || true
                '''
            }
        }
    }
}