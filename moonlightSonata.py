# The first twelve measures (bars) of Beethoven's Moonlight Sonata taken from:
# https://www.music-scores.com/sheet-music.php?download=Beethoven_Moonlight_Sonata_easy
melody1 = "|A3,D3,F3,A3,D3,F3,A3,D3,F3,A3,D3,F3,|A3,D3,F3,A3,D3,F3,A3,D3,F3,A3,D3,F3,|Bb3,D3,F3,Bb3,D3,F3,Bb3,Eb3,G3,Bb3,Eb3,G3,|A3,C#3,G3,A3,D3,F3,A3,D3,E3,G3,C#3,E3,|F3,A3,D3,A3,D3,F3,A3,D3,F3,A3,D3,F3,|A3,E3,G3,A3,E3,G3,A3,E3,G3,A3,E3,G3"
rhythm1 = "|D2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,|C2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,|Bb2, 0, 0,  0, 0, 0, G2,  0, 0,  0,  0, 0,|A2,  0, 0, 0, 0, 0,A2, 0, 0, 0,  0, 0,|A2,D2, 0, 0, 0, 0, 0, 0, 0,A3, 0,A3,|A2,C#2,0, 0, 0, 0, 0, 0, 0,A3, 0,A3"
melody2 = "|A3,D3,F3,A3,D3,F3,Bb3,D3,G3,Bb3,D3,G3,|A3,C3,F3,A3,C3,F3,Gb3,C3,E3,C3,C3,E3,|A3,C3,F3,A3,C3,F3,A3,C3,F3,A3,C3,F3,|Ab3,C3,F3,Ab3,C3,F3,Ab3,C3,F3,Ab3,C3,F3|Ab3,C3,Gb3,Ab3,C3,Gb3,Ab3,C3,Gb3,Ab3,C3,Gb3|Ab3,Db3,F3,Ab3,C3,F3,Ab3,D3,F3,G3,D3,F3"
rhythm2 = "|D2, 0, 0, 0, 0, 0, G2, 0, 0,  0, 0, 0,|C2, 0, 0, 0, 0, 0, C3, 0, 0,Bb2,0, 0,|F2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,|F2,  0, 0,  0, 0, 0,  0, 0, 0,  0, 0, 0|Eb2,  0,  0,  0, 0,  0,  0, 0,  0,  0, 0, 0|Db2,  0, 0,  C3,0, 0,B#2, 0, 0, 0, 0, 0"

notesPerMeasure = 12
# See https://newt.phys.unsw.edu.au/jw/notes.html for context
noteFreqDict = {'C2':65,  'C#2':69,  'Db2':73, 'D2':73,   'Eb2':77, 'E2':82,  'F2':87,   'G2':98,   'A2':110, 'Bb2':117, 'B2':123, 'B#2':131,
                'C3':131, 'C#3':139, 'Db3':139,'D3':147, 'Eb3':156, 'E3':165, 'F3':175, 'Gb3':185, 'G3':196, 'Ab3':208, 'A3':220, 'Bb3':233, 'B3':247,
                'C4':262, 'D4':294,  'E4':330, 'F4':349,  'G4':392, 'A4':440, 'Bb4':466, 'B4':494,
                'C5':523, 'D5':587,  'E5':659, '0':0,
                }

def convertMeasuresToString(measures: list) -> str:
    s = ''
    for measure in measures:
        for note in measure:
            s += f'{note}, '
    return s[:-2]

def processMeasures(*args: str) -> list:
    measures = [validateAndConvertMeasures(measures) for measures in args]
    # flatten all the measures
    return [measure for mlist in measures for measure in mlist]

def validateAndConvertMeasures(measures: list) -> list:
    nmeasures = []
    measures = [measure for measure in measures.split('|') if len(measure)]
    measures = [measure.split(',') for measure in measures]
    for measure in measures:
        #print(measure)
        measure = [note.strip() for note in measure]
        nm = [noteFreqDict.get(note) for note in measure if len(note)]
        #print(nm)
        try:
            assert(len(nm) == notesPerMeasure)
        except Exception as e:
            print(f'ERROR: {nm} has length {len(nm)}')
            raise(e)
        nmeasures.append(nm)
    return nmeasures

if __name__ == '__main__':
    # We have two voices - the LH piano rhythm and the RH piano melody
    melody = convertMeasuresToString(processMeasures(melody1,melody2))
    print(f"melody:\n{melody}")
    rhythm = convertMeasuresToString(processMeasures(rhythm1,rhythm2))
    print(f"rhythm:\n{rhythm}")
    nMelodyNotes = len(melody.split(','))
    nRhythmNotes = len(rhythm.split(','))
    assert(nMelodyNotes == nRhythmNotes)
    print(f"length of music = {nMelodyNotes} notes, {int(nMelodyNotes/notesPerMeasure)} measures of length {notesPerMeasure} notes per measure")