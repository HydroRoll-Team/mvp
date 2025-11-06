use clap::Parser;

#[derive(Parser, Debug)]
#[command(name = "mt")]
struct Args {
    #[arg(short, long)]
    name: String,
}

fn main() {
    let args = Args::parse();
    println!("Hello from CLI, {}!", args.name);
}