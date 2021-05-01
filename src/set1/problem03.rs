use crate::common::challenge;
use crate::common::text;

pub static INFO: challenge::INFO = challenge::INFO {
    no:         3,
    title:      "Single byte XOR",
    help:       "",
    execute_fn: interactive
};

pub fn interactive() -> i32 {
    let input = match hex::decode(String::from("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")) {
        Ok(res) => res,
        Err(_) => return exit_err!()
    };

    match text::find_best_xor_match(&input) {
        Some(result) => {
            println!("Best match was {:?} with score {:?}", result.result, result.score);
        },
        None => println!("No match found")
    }

    exit_ok!()
}
