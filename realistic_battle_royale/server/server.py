import asyncio
import json

class BattleRoyaleServer:
    def __init__(self, host='0.0.0.0', port=8888):
        self.host = host
        self.port = port
        self.players = {} # id: {position, rotation, health, etc}
        self.max_players = 250

    async def handle_client(self, reader, writer):
        addr = writer.get_extra_info('peername')
        player_id = f"{addr[0]}:{addr[1]}"
        print(f"New player connected: {player_id}")
        
        self.players[player_id] = {
            "pos": [0, 0, 0],
            "rot": [0, 0, 0],
            "health": 100,
            "platform": "Unknown" # Will be updated on first message
        }

        try:
            while True:
                data = await reader.read(1024)
                if not data:
                    break
                
                message = json.loads(data.decode())
                # Update player state
                if message['type'] == 'update':
                    self.players[player_id].update(message['data'])
                
                # Broadcast state to all players (Simplified)
                response = json.dumps({
                    "type": "state_update",
                    "players": self.players
                }).encode()
                
                writer.write(response)
                await writer.drain()

        except Exception as e:
            print(f"Error handling player {player_id}: {e}")
        finally:
            print(f"Player disconnected: {player_id}")
            del self.players[player_id]
            writer.close()

    async def run(self):
        server = await asyncio.start_server(self.handle_client, self.host, self.port)
        addr = server.sockets[0].getsockname()
        print(f'Server running on {addr}')

        async with server:
            await server.serve_forever()

if __name__ == "__main__":
    server = BattleRoyaleServer()
    asyncio.run(server.run())
