pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Código obtenido desde GitHub'
            }
        }

        stage('Docker Version') {
            steps {
                sh 'docker version'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t urban-routes-tests:${BUILD_NUMBER} .'
            }
        }

        stage('Run Automated Tests') {
            steps {
                sh 'docker run --rm urban-routes-tests:${BUILD_NUMBER}'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completado: pruebas automatizadas aprobadas'
        }

        failure {
            echo 'Pipeline fallido: revisar los logs de Jenkins'
        }
    }
}