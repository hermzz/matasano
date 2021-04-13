
pub type ExitCode = i32;

macro_rules! exit_ok {
    ( ) => ( 0 );
}

macro_rules! exit_err {
    ( ) => ( 1 );
}

