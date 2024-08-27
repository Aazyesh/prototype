const { createHash } = require("crypto");

function hash(input) {
    return createHash('sha256').update(input).digest("hex");
}

let password = "Hey there";
const hash1 = hash(password);
console.log(hash1);



const { scryptSync, randomBytes, timingSafeEqual } = require('crypto')

function signup(email, password){
    const salt = randomBytes(16).toString('hex');
    const hashedPassword = scryptSync(password, salt, 64).toString('hex');
    console.log(hashedPassword)
    console.log(salt)
    const user = { email, password: `${salt}:${hashedPassword}` };
    return user;
}
function login(email, password){

    const [salt, key] = user.password.split(':')
    const hashedBuffer = scryptSync(password, salt, 64);

    const keyBuffer = Buffer.from(key, 'hex');
}
