pipeline {
  agent any
  environment {
    IMAGE_NAME = "obliviobvious/sage-auth"
  }
  stages {
    stage('Build') {
      steps {
        sh 'docker build -t $IMAGE_NAME .'
      }
    }
    stage('Test') {
      steps {
        sh 'echo Running some tests...'
      }
    }
    stage('Publish') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'DockerHubLogin', passwordVariable: 'password', usernameVariable: 'username')]) {
          sh 'docker login -u ${username} -p ${password}'
          sh 'docker push $IMAGE_NAME'
        }
      }
    }
    stage('Deploy') {
      steps {
        sh 'echo Running kubectl apply'
      }
    }
  }
}