use crate::common::challenge;
use crate::common::text;
use crate::common::file;

pub static INFO: challenge::INFO = challenge::INFO {
    no:         4,
    title:      "Detect single-character XOR",
    help:       "",
    execute_fn: interactive
};

pub fn interactive() -> i32 {
    if let Ok(lines) = file::read_lines("files/4.txt") {
        let mut best_match = text::Match { result: String::from(""), score: 0.0 };

        for line in lines {
            if let Ok(hash) = line {
                match hex::decode(hash) {
                    Ok(result) => {
                        match text::find_best_xor_match(&result.to_vec()) {
                            Some(result) => {
                                if best_match.result.len() == 0 || result.score < best_match.score {
                                    best_match = result;
                                }
                            },
                            None => {}
                        }
                    },
                    Err(_) => {}
                }
            }
        }

        if best_match.score == 0.0 {
            println!("No good match found!");
            return exit_err!();
        }

        println!("Best match was {:?} with score {:?}", best_match.result, best_match.score);
    }

    exit_ok!()
}