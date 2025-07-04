pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'ls -al'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'python3 -m pytest test.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh 'python3 app.py'
            }
        }
    }

    post {
        success {
            echo "Successful"
        }

        failure {
            echo "Failed"
        }

        always {
            echo "Pipeline completed"
        }
    }
}
