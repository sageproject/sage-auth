pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        sh 'echo Running some tests...'
      }
    }
    stage('Deploy') {
      steps {
        sh 'echo Running kubectl apply'
      }
    }
  }
}