use std::env;

use serenity::{all::GatewayIntents, async_trait};
use serenity::prelude::*;

mod commands;

type Error = Box<dyn std::error::Error + Send + Sync>;
type Context<'a> = poise::Context<'a, Data, Error>;
pub struct Data {}

struct Handler;

#[async_trait]
impl EventHandler for Handler {

}

#[tokio::main]
async fn main() {
    let _ = dotenvy::dotenv(); // .env file not required if loading from CLI

    let options = poise::FrameworkOptions {
        commands: vec![commands::lookup_musicbrainz()],
        ..Default::default()
    };
    let framework = poise::Framework::builder()
        .setup(move |ctx: &serenity::prelude::Context, _ready: &serenity::model::prelude::Ready, framework: &poise::Framework<Data, _>| {
            Box::pin(async move {
                println!("Logged in as {}", _ready.user.name);
                poise::builtins::register_globally(ctx, &framework.options().commands).await?;
                Ok(Data {})
            })
        }).options(options).build();

    let token: String = env::var("DISCORD_TOKEN").expect("Expected a token in the environment");
    let intents: GatewayIntents = GatewayIntents::empty();
    
    let mut client: Client = Client::builder(&token, intents).framework(framework).event_handler(Handler).await.expect("Error creating client");
    if let Err(why) = client.start().await {
        println!("Client error: {why:?}");
    }
}
