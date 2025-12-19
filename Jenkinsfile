pipeline {
  agent any

  environment {
    APP_IMAGE = "cinema_final:1.0"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t ${APP_IMAGE} .'
      }
    }

    stage('Deploy with Docker Compose') {
      steps {
        sh 'docker compose down || true'
        sh 'docker compose up -d'
        sh 'docker compose ps'
      }
    }

    stage('Smoke Test') {
      steps {
        sh 'sleep 3'
        sh 'curl -I http://localhost:5001 | head -n 1'
      }
    }
  }

  post {
    always {
      sh 'docker ps'
    }
  }
}
