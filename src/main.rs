use clap::Parser;
use tklog::{Async::Log, LogOption, LOG};

#[derive(Parser, Debug)]
#[command(name = "mt")]
struct Args {
    #[arg(short, long)]
    name: String,
}

fn main() {
    let args = Args::parse();
    let log = Log::new();
    tklog::info!(&format!("Hello from CLI, {}!", args.name));
}
