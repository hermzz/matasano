use hex::FromHexError;
use core::fmt;
use std::error;

type Result<T> = std::result::Result<T, XorError>;

#[derive(Debug)]
pub enum XorError {
    LengthMismatch,
    Hex(FromHexError)
}

impl fmt::Display for XorError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match *self {
            XorError::LengthMismatch =>
                write!(f, "Make sure both strings are of equal length"),
            XorError::Hex(ref e) => e.fmt(f),
        }
    }
}

impl error::Error for XorError {
    fn source(&self) -> Option<&(dyn error::Error + 'static)> {
        match *self {
            XorError::LengthMismatch => None,
            XorError::Hex(ref e) => Some(e),
        }
    }
}

impl From<FromHexError> for XorError {
    fn from(err: FromHexError) -> XorError {
        XorError::Hex(err)
    }
}

pub fn hex(input: String, xor: String) -> Result<String> {
    let decoded_input = hex::decode(input)?;
    let decoded_xor = hex::decode(xor)?;

    if decoded_input.len() != decoded_xor.len() {
        return Err(XorError::LengthMismatch);
    }

    let mut result: Vec<u8> = Vec::new();

    let mut pos = 0;
    while pos < decoded_input.len() {
        result.push(decoded_input[pos] ^ decoded_xor[pos]);

        pos += 1;
    }

    Ok(hex::encode(result))
}