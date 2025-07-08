pipeline {
    agent any

    parameters {
        string(name: 'BRANCH_NAME', defaultValue: 'master', description: 'Git branch to build')
        booleanParam(name: 'RUN_TESTS', defaultValue: true, description: 'Run unit tests?')
        choice(name: 'DEPLOY_ENV', choices: ['dev', 'staging', 'prod'], description: 'Deploy environment')
    }

    stages {
        stage('Info') {
            steps {
                echo "Branch: ${params.BRANCH_NAME}"
                echo "Run Tests: ${params.RUN_TESTS}"
                echo "Deploy to: ${params.DEPLOY_ENV}"
            }
        }

        stage('Conditional Test') {
            when {
                expression { return params.RUN_TESTS }
            }
            steps {
                echo '🧪 Running tests...'
                sh 'pytest'
            }
        }
    }
}
