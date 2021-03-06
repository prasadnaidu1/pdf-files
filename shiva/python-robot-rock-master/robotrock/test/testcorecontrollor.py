#! usr/bin/env python

''' testcorecontrollor.py
    Author: Michael Beenen <beenen34@cs.washington.edu>
    Unit test for CoreControllor.
'''
import unittest
import sys

class TestCoreController(unittest.TestCase):
    def setUp(self):
        
        # Stub class for Metronome 
        class Metronome(object):
            
            def __init__(self):
                self.tempo = 60
            
            def setTempo(self,tempo):
                self.tempo = tempo
        
        # Stub class for AudioDriver
        class AudioDriver(object):
            
            def __init__(self):
                self.playing = False
            
            def play(self):
                self.playing = True
            
            def pause(self):
                self.playing = False
            
            def isPlaying(self):
                return self.playing
        
        # Stub class for Conductor
        class Conductor(object):
            
            def __init__(self):
                self.ensemble = []
                self.musician_staffs = {}
                
            def addMusician(self, musician):
                self.ensemble.append(musician)
                self.musician_staffs[musician] = None
            
            def removeMusician(self, musician):
                self.ensemble.remove(musician)
               
        class Parser(object):

            def registerStaff(self, staff):
                return True
 
            def unregisterStaff(self, staff):
                return True

        class MusicianDirectory(object):
            
            def __init__(self):
                pass
                
            def filterMusicianList(self, tags):
                if tags == set(['acoustic']):
                    return ['acousticguitar']
                if tags == set(['percussion']):
                    return ['handdrum', 'metronome']
                if tags == set(['acoustic', 'electric']):
                    return []
                    
            def validTags(self, tags):
                if tags == set(['acoustic']):
                    return ['string']
                if tags == set(['string']):
                    return ['acoustic', 'electric']
                if tags == set(['percussion']):
                    return []
            
        
        self.metronome = Metronome()
        self.audio_driver = AudioDriver()
        self.song_info = songinfo.SongInfo()
        self.conductor = Conductor()
        self.parser = Parser()
        self.musiciandirectory = MusicianDirectory()
        self.corecontroller = corecontroller.CoreController(self.audio_driver, \
                self.metronome, self.parser, self.conductor, self.song_info, \
                self.musiciandirectory)
    def testplay(self):
        self.corecontroller.play()
        self.assertTrue(self.audio_driver.isPlaying())
    
    def testpause(self):
        self.corecontroller.play()
        self.corecontroller.pause()
        self.assertFalse(self.audio_driver.isPlaying())
    
    def testsetTempo(self):
        # Random input values
        self.corecontroller.setTempo(120)
        self.assertEqual(self.metronome.tempo, 120)
        self.corecontroller.setTempo(93)
        self.assertEqual(self.metronome.tempo, 93)
        self.corecontroller.setTempo(180)
        self.assertEqual(self.metronome.tempo, 180)
        self.corecontroller.setTempo(76)
        self.assertEqual(self.metronome.tempo, 76)
        
        # Boundary Cases below
        self.corecontroller.setTempo(208)
        self.assertEqual(self.metronome.tempo, 208)
        self.corecontroller.setTempo(209)
        self.assertEqual(self.metronome.tempo, 208)
        self.corecontroller.setTempo(40)
        self.assertEqual(self.metronome.tempo, 40)
        self.corecontroller.setTempo(39)
        self.assertEqual(self.metronome.tempo, 40)
        self.corecontroller.setTempo(-1)
        self.assertEqual(self.metronome.tempo, 40)
    
    def testupdateTimeSignature(self):
        # Test valid inputs
        self.corecontroller.updateTimeSignature((3, 4))
        info = self.corecontroller.song_info.measureInfo()
        self.assertEqual(info['time_signature'], (3, 4))
        self.corecontroller.updateTimeSignature((2, 4))
        info = self.corecontroller.song_info.measureInfo()
        self.assertEqual(info['time_signature'], (2, 4))
        
        # Test invalid inputs, ensure no side effects
        self.corecontroller.updateTimeSignature((0, 2))
        info = self.corecontroller.song_info.measureInfo()
        self.assertEqual(info['time_signature'], (2, 4))
        self.corecontroller.updateTimeSignature((5, 6, 7))
        info = self.corecontroller.song_info.measureInfo()
        self.assertEqual(info['time_signature'], (2, 4))
    
    def testupdateKeySignature(self):
        # Test valid inptus
        self.corecontroller.updateKeySignature(('C#', 'major'))
        info = self.corecontroller.song_info.measureInfo()
        self.assertEqual(info['key_signature'], ('C#', 'major'))
        self.corecontroller.updateKeySignature(('D', 'minor'))
        info = self.corecontroller.song_info.measureInfo()
        self.assertEqual(info['key_signature'], ('D', 'minor'))
        # Test assertion, ensure no side effects
        self.corecontroller.updateKeySignature(('C', 'minor', 'Too long'))
        info = self.corecontroller.song_info.measureInfo()
        self.assertEqual(info['key_signature'], ('D', 'minor'))
    
    def testaddMusician(self):
        self.corecontroller.addMusician('Guitar')
        self.assertEqual(self.conductor.ensemble, ['Guitar'])
        self.corecontroller.addMusician('Drum')
        self.assertEqual(self.conductor.ensemble, ['Guitar', 'Drum'])
    
    def testremoveMusician(self):
        self.conductor.ensemble = ['Piano', 'Guitar', 'Drum']
        self.conductor.musician_staffs = { 
                                         'Piano': None,
                                         'Guitar': None,
                                         'Drum': None
                                         }   
        self.corecontroller.removeMusician('Guitar')
        self.assertEqual(self.conductor.ensemble, ['Piano', 'Drum'])
        self.corecontroller.removeMusician('Drum')
        self.assertEqual(self.conductor.ensemble, ['Piano'])
        
        # Test no side effect when musician is not in ensemble
        self.corecontroller.removeMusician('Drum')
        self.assertEqual(self.conductor.ensemble, ['Piano'])
        
        self.corecontroller.removeMusician('Piano')
        self.assertEqual(self.conductor.ensemble, [])
    
    def testfilterMusicianList(self):
        list = self.corecontroller.filterMusicianList(['acoustic'])
        self.assertEqual(['acousticguitar'], list)
        list = self.corecontroller.filterMusicianList(['percussion'])
        self.assertEqual(['handdrum', 'metronome'], list)
        list = self.corecontroller.filterMusicianList(['acoustic', 'electric'])
        self.assertEqual(list, [])
        
    def testvalidTags(self):
        list = self.corecontroller.validTags(set(['acoustic']))
        self.assertEqual(list, ['string'])
        list = self.corecontroller.validTags(set(['string']))
        self.assertEqual(list, ['acoustic', 'electric'])
        list = self.corecontroller.validTags(set(['percussion']))
        self.assertEqual(list, [])
        
    
if __name__ == '__main__':
    sys.path.append('../robotrock/')
    import corecontroller
    import songinfo
    unittest.main()


