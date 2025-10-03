pipeline{
    agent any
    stages{
        stage('version'){
            steps{
                bat 'python --version'
                bat 'playwright install'
            }
        }

        stage('attendance_MARK_IN'){
            steps{
                bat 'attendance_MARK_IN.py'
            }
        }
    }
}