import requests, discord

def lookupLink(link: str):
    result = requests.get('https://api.song.link/v1-alpha.1/links', params={'songIfSingle': 'true', 'url': requests.utils.quote(link, safe='')})
    if result.status_code != 200:
        raise Exception()
    res = SongResult(result.json())

    return res

class Links:
    def __init__(self, links):
        self.url = links.get('url')
        self.native_mobile_uri = links.get('nativeAppUriMobile')
        self.native_desktop_uri = links.get('nativeAppUriDesktop')

class SongResult:
    def __init__(self, data):
        self.link = data.get('pageUrl')

        # basic info
        album_info = data.get('entitiesByUniqueId').get(data['entityUniqueId'])
        self.source = album_info.get('apiProvider')
        self.type = album_info.get('type')
        self.title = album_info.get('title')
        self.artist = album_info.get('artistName')
        self.thumb_url = album_info.get('thumbnailUrl')
        self.thumb_dimensions = (album_info.get('thumbnailWidth'), album_info.get('thumbnailHeight'))

        self.platforms = {}
        platformlinks = data['linksByPlatform']
        for platform in platformlinks:
            self.platforms[platform] = Links(platformlinks[platform])

listed_platforms = {
    'youtube': 'Youtube',
    'appleMusic': 'Apple Music',
    'spotify': 'Spotify'
}

def buildEmbed(song: SongResult):
    embed = discord.Embed(
        title = f'{song.title}',
        description = f'{song.type} by {song.artist} - [view on song.link]({song.link})',
        color = discord.Colour.blurple()
    )
    embed.set_thumbnail(url = song.thumb_url)

    for platform in song.platforms:
        if platform in listed_platforms:
            embed.add_field(name = f"{listed_platforms.get(platform)}", value = f"[Stream]({song.platforms[platform].url})")

    return embed