#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Qam Example
# Generated: Tue Apr  3 11:28:36 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import numpy
import sys
import time
from gnuradio import qtgui


class qam_example(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Qam Example")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Qam Example")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "qam_example")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################

        self.variable_constellation_0 = variable_constellation_0 = digital.constellation_qpsk().base()

        self.samp_rate = samp_rate = 500e3
        self.freq = freq = 25e3

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(1.9e9, 0)
        self.uhd_usrp_source_0.set_gain(60, 0)
        self.uhd_usrp_source_0.set_antenna('RX2', 0)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(1.9e9, 0)
        self.uhd_usrp_sink_0.set_gain(20, 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        self.digital_qam_demod_0 = digital.qam.qam_demod(
          constellation_points=4,
          differential=True,
          samples_per_symbol=8,
          excess_bw=0.009,
          freq_bw=0,
          timing_bw=0,
          phase_bw=0,
          mod_code="gray",
          verbose=False,
          log=False,
          )
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(8, 0.002, (firdes.root_raised_cosine(128, 128, 1.0/float(4), 0.35, 45*128)), 32, 8, 1.5, 1)
        self.digital_constellation_modulator_0 = digital.generic_mod(
          constellation=variable_constellation_0,
          differential=True,
          samples_per_symbol=8,
          pre_diff_code=True,
          excess_bw=0.009,
          verbose=False,
          log=False,
          )
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((5, ))
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 1)
        self.blocks_file_sink_1_0 = blocks.file_sink(gr.sizeof_gr_complex*1, './qpsk_tx_constellation.log', False)
        self.blocks_file_sink_1_0.set_unbuffered(False)
        self.blocks_file_sink_1 = blocks.file_sink(gr.sizeof_gr_complex*1, './qpsk_rx_constellation.log', False)
        self.blocks_file_sink_1.set_unbuffered(False)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_float*1, './qpsk_original_signal.log', False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_float*1, './qpsk_rx_decoded_signal.log', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_char_to_float_1 = blocks.char_to_float(1, 1)
        self.analog_random_source_x_0 = blocks.vector_source_s(map(int, numpy.random.randint(0, 2, 1000000)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_short_to_float_0, 0))
        self.connect((self.blocks_char_to_float_1, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_float_to_char_0, 0), (self.digital_constellation_modulator_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_file_sink_1_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.blocks_short_to_float_0, 0), (self.blocks_float_to_char_0, 0))
        self.connect((self.digital_constellation_modulator_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.blocks_file_sink_1, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_qam_demod_0, 0))
        self.connect((self.digital_qam_demod_0, 0), (self.blocks_char_to_float_1, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "qam_example")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_variable_constellation_0(self):
        return self.variable_constellation_0

    def set_variable_constellation_0(self, variable_constellation_0):
        self.variable_constellation_0 = variable_constellation_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq


def main(top_block_cls=qam_example, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
