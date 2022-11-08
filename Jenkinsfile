pipeline {
  agent any
  environment {
    IMAGE_NAME = "obliviobvious/sage-auth"
    img = ''
  }
  stages {
    stage('Build') {
      steps {
        script {
          img = docker.build IMAGE_NAME
        }
      }
    }
    stage('Test') {
      steps {
        sh 'echo Running some tests...'
      }
    }
    stage('Publish') {
      steps {
        script {
          img.push("0.0.${env.BUILD_ID}")
          img.push("latest")
        }
      }
    }
    stage('Deploy') {
      steps {
        sh 'kubectl get all'
      }
    }
  }
}