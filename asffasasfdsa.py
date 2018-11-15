               memberz = []
                for member in message.server.members:
                    memberz.append(member)
                for member in memberz:
                    if str(member.mention) in commands[1]:
                        k = ("""
:ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:                 
                                                  %s      
                        """ % (member.mention))
                        x = ("""
:ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:                 
                                                  %s      
                        """ % (member.mention))
                        a = ("""
:ok_hand:            :smiley:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:                 
                                                  %s      
                        """ % (member.mention))
                        b = ("""
:ok_hand:            :grimacing:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:                
                                                  %s      
                        """ % (member.mention))
                        c = ("""
:ok_hand:            :persevere:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:                 
                                                  %s      
                        """ % (member.mention))
                        d = ("""
:ok_hand:            :confounded:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:                 
                                                  %s      
                        """ % (member.mention))
                        e = ("""
:ok_hand:            :tired_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:                 
                                                  %s      
                        """ % (member.mention))
                        f = ("""
:ok_hand:            :weary:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:= D:sweat_drops:
             :trumpet:      :eggplant:                 
                                                  %s      
                        """ % (member.mention))
                        t = ("""
:ok_hand:            :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
                                                  %s      
                        """ % (member.mention))
                        g = ("""
:ok_hand:            :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
                                                  %s      
                        """ % (member.mention))
                        string = [k,a,b,c,d,e,f,t,g]
                        for z in string:
                            await client.edit_message(message,z)
                            await asyncio.sleep(.3)
                await client.delete_message(message)
