pipeline {
   
    agent any
    // agent {
    //     dockerfile {
    //         filename 'Dockerfile'
    //         dir '.'
    //     }
    // }

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
                sh 'touch mohamed.txt'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh 'echo "mohamed is here ">>mohamed.txt'
            }
        }

       stage('excute') {
            steps {
                echo 'Excuting....'
                sh 'cat mohamed.txt'
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
