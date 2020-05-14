use hex::FromHexError;
use base64;
use hex;

pub fn hex_to_base64(input: &String) -> Result<String, FromHexError> {
    match hex::decode(input) {
        Ok(decoded) => Ok(base64::encode(decoded)),
        Err(e) => Err(e)
    }
}