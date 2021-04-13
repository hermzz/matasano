use crate::common::err;

pub struct INFO {
    pub no:         u32,
    pub title:      &'static str,
    pub help:       &'static str,
    pub execute_fn: fn() -> err::ExitCode
}