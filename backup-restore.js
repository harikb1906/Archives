const aws = require('aws-sdk')
const fs = require('fs')
const { backupUsers, restoreUsers } = require('cognito-backup-restore')

currentTime = new Date().toISOString().replace(':', '-').replace(':', '-')
ENV = (process.env.ENV || 'ENV')
// config starts
/* Setting the AWS region, access key, and secret access key. */
aws.config.update({
  region: 'eu-west-1',
})
const cognitoId = ''
const cognitoIdOther = ''
const s3BucketName = ''
// config ends

/* Creating a new instance of the CognitoIdentityServiceProvider and S3 classes. */
const provider = new aws.CognitoIdentityServiceProvider()
const s3 = new aws.S3()
/* Creating the file path and file name for the backup file. */
const folderName = '/tmp'
const fileName = cognitoId +'.' +currentTime +'.json'
const filePathName = folderName + '/' + fileName
const tempFileName = folderName + '/tepBkp.json'

/**
 * It takes a file path and file name as arguments, creates a read stream of the file, and uploads it
 * to an S3 bucket
 */
async function uploadFileOnS3(filePathName, fileName) {
  const fileContent = fs.createReadStream(`${filePathName}`)
  const params = {
    Bucket: s3BucketName,
    Key: ENV + '/' +fileName,
    Body: fileContent,
  }
  try {
    const response = await s3.upload(params).promise()
    console.log('Response: ', response)
    return response
  } catch (err) {
    console.log(err)
  }
}

/**
 * It takes a file path and file name, and returns the file from S3.
 */
async function getFileS3(fileName) {
  try {
    const params = {
      Bucket: s3BucketName,
      Key: fileName,
    }

    const data = await s3.getObject(params).promise()
    return Promise.resolve(data)
  } catch (err) {
    return Promise.reject(err)
  }
}

function backup() {
  backupUsers(provider, cognitoId, folderName)
    .then(async () => {
      await uploadFileOnS3(filePathName, fileName)
      console.log(`Backup completed`)
      // await fs.unlink(filePathName)
    })
    .catch(console.error)
}

async function restore() {
  /* Getting the file from S3. */
  const s3File = await getFileS3(fileName)
  /* Writing the file to the local file system. */
  await fs.writeFileSync(tempFileName, s3File.Body)
  // restore to cognito
  /*
  restoreUsers(provider, cognitoIdOther, tempFileName)
    .then(() => {})
    .catch(console.error)
    .finally(async () => {
      await fs.unlink(tempFileName)
      console.log(`Restore completed`)
    })
    */
}

/* Exporting the functions backup and restore. */
module.exports = {
  backup,
  restore,
}
