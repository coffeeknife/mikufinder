use crate::{ Context, Error };

#[poise::command(prefix_command, slash_command)]
pub async fn lookup_musicbrainz(
    ctx: Context<'_>, 
    #[description = "MusicBrainz ID to retrieve info for"] mbid: String
) -> Result<(), Error> {
    ctx.say(format!("You're looking up mbid: {mbid}")).await?;
    Ok(())
} 