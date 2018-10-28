#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: UHD FFT
# Author: Example
# Description: UHD FFT Waveform Plotter
# Generated: Sat Apr 14 13:08:00 2018
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
from PyQt4.QtCore import QObject, pyqtSlot
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import numpy
import sip
import sys
import threading
import time
from gnuradio import qtgui


class Testin(gr.top_block, Qt.QWidget):

    def __init__(self, antenna='RX2', args='', fft_size=1024, freq=2.45e9, gain=20, samp_rate=1e6, spec='', stream_args='', update_rate=.1, wire_format=''):
        gr.top_block.__init__(self, "UHD FFT")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("UHD FFT")
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

        self.settings = Qt.QSettings("GNU Radio", "Testin")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.antenna = antenna
        self.args = args
        self.fft_size = fft_size
        self.freq = freq
        self.gain = gain
        self.samp_rate = samp_rate
        self.spec = spec
        self.stream_args = stream_args
        self.update_rate = update_rate
        self.wire_format = wire_format

        ##################################################
        # Variables
        ##################################################
        self.freq_c = freq_c = freq
        self.chan0_lo_locked = chan0_lo_locked = uhd.sensor_value("", False, "")
        self.usrp_device_info = usrp_device_info = uhd.get_version_string()
        self.uhd_version_info = uhd_version_info = uhd.get_version_string()
        self.samp_rate_ = samp_rate_ = samp_rate
        self.lo_locked_probe = lo_locked_probe = chan0_lo_locked.to_bool()
        self.gain_ = gain_ = gain
        self.current_freq_c = current_freq_c = freq_c
        self.audio_decim = audio_decim = 10
        self.ant = ant = antenna

        ##################################################
        # Blocks
        ##################################################
        self._samp_rate__tool_bar = Qt.QToolBar(self)
        self._samp_rate__tool_bar.addWidget(Qt.QLabel('Sampling Rate'+": "))
        self._samp_rate__line_edit = Qt.QLineEdit(str(self.samp_rate_))
        self._samp_rate__tool_bar.addWidget(self._samp_rate__line_edit)
        self._samp_rate__line_edit.returnPressed.connect(
        	lambda: self.set_samp_rate_(eng_notation.str_to_num(str(self._samp_rate__line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._samp_rate__tool_bar, 3,2,1,2)
        self._gain__range = Range(0, 31.5, .5, gain, 200)
        self._gain__win = RangeWidget(self._gain__range, self.set_gain_, 'RX Gain', "counter_slider", float)
        self.top_grid_layout.addWidget(self._gain__win, 2,0,1,4)
        self._freq_c_tool_bar = Qt.QToolBar(self)
        self._freq_c_tool_bar.addWidget(Qt.QLabel('RX Tune Frequency'+": "))
        self._freq_c_line_edit = Qt.QLineEdit(str(self.freq_c))
        self._freq_c_tool_bar.addWidget(self._freq_c_line_edit)
        self._freq_c_line_edit.returnPressed.connect(
        	lambda: self.set_freq_c(eng_notation.str_to_num(str(self._freq_c_line_edit.text().toAscii()))))
        self.top_grid_layout.addWidget(self._freq_c_tool_bar, 3,0,1,2)
        self._ant_options = ('RX2', 'TX/RX', 'J1', 'J2', )
        self._ant_labels = ('RX2', 'TX/RX', 'J1', 'J2', )
        self._ant_tool_bar = Qt.QToolBar(self)
        self._ant_tool_bar.addWidget(Qt.QLabel('Antenna'+": "))
        self._ant_combo_box = Qt.QComboBox()
        self._ant_tool_bar.addWidget(self._ant_combo_box)
        for label in self._ant_labels: self._ant_combo_box.addItem(label)
        self._ant_callback = lambda i: Qt.QMetaObject.invokeMethod(self._ant_combo_box, "setCurrentIndex", Qt.Q_ARG("int", self._ant_options.index(i)))
        self._ant_callback(self.ant)
        self._ant_combo_box.currentIndexChanged.connect(
        	lambda i: self.set_ant(self._ant_options[i]))
        self.top_grid_layout.addWidget(self._ant_tool_bar, 4,2,1,2)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join((args, "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate_)
        self.uhd_usrp_source_0.set_center_freq(float(freq_c), 0)
        self.uhd_usrp_source_0.set_gain(gain_, 0)
        self.uhd_usrp_source_0.set_antenna(ant, 0)
        self.uhd_usrp_source_0.set_bandwidth(samp_rate, 0)
        self.volume = blocks.multiply_const_vcc((20, ))
        self._usrp_device_info_tool_bar = Qt.QToolBar(self)

        if None:
          self._usrp_device_info_formatter = None
        else:
          self._usrp_device_info_formatter = lambda x: repr(x)

        self._usrp_device_info_tool_bar.addWidget(Qt.QLabel('Device Information'+": "))
        self._usrp_device_info_label = Qt.QLabel(str(self._usrp_device_info_formatter(self.usrp_device_info)))
        self._usrp_device_info_tool_bar.addWidget(self._usrp_device_info_label)
        self.top_grid_layout.addWidget(self._usrp_device_info_tool_bar, 1,2,1,2)

        self._uhd_version_info_tool_bar = Qt.QToolBar(self)

        if None:
          self._uhd_version_info_formatter = None
        else:
          self._uhd_version_info_formatter = lambda x: str(x)

        self._uhd_version_info_tool_bar.addWidget(Qt.QLabel('UHD Version'+": "))
        self._uhd_version_info_label = Qt.QLabel(str(self._uhd_version_info_formatter(self.uhd_version_info)))
        self._uhd_version_info_tool_bar.addWidget(self._uhd_version_info_label)
        self.top_grid_layout.addWidget(self._uhd_version_info_tool_bar, 1,0,1,2)

        self.qtgui_sink_x_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	freq, #fc
        	samp_rate_, #bw
        	"", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_sink_x_0_win)

        self.qtgui_sink_x_0.enable_rf_freq(False)



        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 200e3, 30e3, firdes.WIN_HANN, 6.76))
        self._lo_locked_probe_tool_bar = Qt.QToolBar(self)

        if None:
          self._lo_locked_probe_formatter = None
        else:
          self._lo_locked_probe_formatter = lambda x: str(x)

        self._lo_locked_probe_tool_bar.addWidget(Qt.QLabel('LO locked'+": "))
        self._lo_locked_probe_label = Qt.QLabel(str(self._lo_locked_probe_formatter(self.lo_locked_probe)))
        self._lo_locked_probe_tool_bar.addWidget(self._lo_locked_probe_label)
        self.top_grid_layout.addWidget(self._lo_locked_probe_tool_bar, 4,0,1,2)


        def _current_freq_c_probe():
            while True:
                val = self.uhd_usrp_source_0.get_sensor('lo_locked')
                try:
                    self.set_current_freq_c(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _current_freq_c_thread = threading.Thread(target=_current_freq_c_probe)
        _current_freq_c_thread.daemon = True
        _current_freq_c_thread.start()


        def _chan0_lo_locked_probe():
            while True:
                val = self.uhd_usrp_source_0.get_sensor('lo_locked')
                try:
                    self.set_chan0_lo_locked(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _chan0_lo_locked_thread = threading.Thread(target=_chan0_lo_locked_probe)
        _chan0_lo_locked_thread.daemon = True
        _chan0_lo_locked_thread.start()

        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_float*1, 'wfbm_rx2.log', False)
        self.blocks_file_sink_0_0.set_unbuffered(False)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, 'wfbm_rx1.log', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.analog_wfm_rcv = analog.wfm_rcv(
        	quad_rate=samp_rate,
        	audio_decimation=10,
        )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_wfm_rcv, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.analog_wfm_rcv, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.low_pass_filter_0, 0), (self.volume, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.low_pass_filter_0, 0))
        self.connect((self.volume, 0), (self.analog_wfm_rcv, 0))
        self.connect((self.volume, 0), (self.blocks_file_sink_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "Testin")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_antenna(self):
        return self.antenna

    def set_antenna(self, antenna):
        self.antenna = antenna
        self.set_ant(self.antenna)

    def get_args(self):
        return self.args

    def set_args(self, args):
        self.args = args

    def get_fft_size(self):
        return self.fft_size

    def set_fft_size(self, fft_size):
        self.fft_size = fft_size

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.set_freq_c(self.freq)
        self.qtgui_sink_x_0.set_frequency_range(self.freq, self.samp_rate_)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.set_gain_(self.gain)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_samp_rate_(self.samp_rate)
        self.uhd_usrp_source_0.set_bandwidth(self.samp_rate, 0)
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 200e3, 30e3, firdes.WIN_HANN, 6.76))

    def get_spec(self):
        return self.spec

    def set_spec(self, spec):
        self.spec = spec

    def get_stream_args(self):
        return self.stream_args

    def set_stream_args(self, stream_args):
        self.stream_args = stream_args

    def get_update_rate(self):
        return self.update_rate

    def set_update_rate(self, update_rate):
        self.update_rate = update_rate

    def get_wire_format(self):
        return self.wire_format

    def set_wire_format(self, wire_format):
        self.wire_format = wire_format

    def get_freq_c(self):
        return self.freq_c

    def set_freq_c(self, freq_c):
        self.freq_c = freq_c
        Qt.QMetaObject.invokeMethod(self._freq_c_line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.freq_c)))
        self.uhd_usrp_source_0.set_center_freq(float(self.freq_c), 0)
        self.set_current_freq_c(self.freq_c)

    def get_chan0_lo_locked(self):
        return self.chan0_lo_locked

    def set_chan0_lo_locked(self, chan0_lo_locked):
        self.chan0_lo_locked = chan0_lo_locked

    def get_usrp_device_info(self):
        return self.usrp_device_info

    def set_usrp_device_info(self, usrp_device_info):
        self.usrp_device_info = usrp_device_info
        Qt.QMetaObject.invokeMethod(self._usrp_device_info_label, "setText", Qt.Q_ARG("QString", self.usrp_device_info))

    def get_uhd_version_info(self):
        return self.uhd_version_info

    def set_uhd_version_info(self, uhd_version_info):
        self.uhd_version_info = uhd_version_info
        Qt.QMetaObject.invokeMethod(self._uhd_version_info_label, "setText", Qt.Q_ARG("QString", self.uhd_version_info))

    def get_samp_rate_(self):
        return self.samp_rate_

    def set_samp_rate_(self, samp_rate_):
        self.samp_rate_ = samp_rate_
        Qt.QMetaObject.invokeMethod(self._samp_rate__line_edit, "setText", Qt.Q_ARG("QString", eng_notation.num_to_str(self.samp_rate_)))
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate_)
        self.qtgui_sink_x_0.set_frequency_range(self.freq, self.samp_rate_)

    def get_lo_locked_probe(self):
        return self.lo_locked_probe

    def set_lo_locked_probe(self, lo_locked_probe):
        self.lo_locked_probe = lo_locked_probe
        Qt.QMetaObject.invokeMethod(self._lo_locked_probe_label, "setText", Qt.Q_ARG("QString", self.lo_locked_probe))

    def get_gain_(self):
        return self.gain_

    def set_gain_(self, gain_):
        self.gain_ = gain_
        self.uhd_usrp_source_0.set_gain(self.gain_, 0)


    def get_current_freq_c(self):
        return self.current_freq_c

    def set_current_freq_c(self, current_freq_c):
        self.current_freq_c = current_freq_c

    def get_audio_decim(self):
        return self.audio_decim

    def set_audio_decim(self, audio_decim):
        self.audio_decim = audio_decim

    def get_ant(self):
        return self.ant

    def set_ant(self, ant):
        self.ant = ant
        self._ant_callback(self.ant)
        self.uhd_usrp_source_0.set_antenna(self.ant, 0)


def argument_parser():
    description = 'UHD FFT Waveform Plotter'
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option, description=description)
    parser.add_option(
        "-A", "--antenna", dest="antenna", type="string", default='RX2',
        help="Set Antenna [default=%default]")
    parser.add_option(
        "-a", "--args", dest="args", type="string", default='',
        help="Set UHD device address args [default=%default]")
    parser.add_option(
        "", "--fft-size", dest="fft_size", type="intx", default=1024,
        help="Set Set number of FFT bins [default=%default]")
    parser.add_option(
        "-f", "--freq", dest="freq", type="eng_float", default=eng_notation.num_to_str(2.45e9),
        help="Set Default Frequency [default=%default]")
    parser.add_option(
        "-g", "--gain", dest="gain", type="eng_float", default=eng_notation.num_to_str(20),
        help="Set Set gain in dB (default is midpoint) [default=%default]")
    parser.add_option(
        "-s", "--samp-rate", dest="samp_rate", type="eng_float", default=eng_notation.num_to_str(1e6),
        help="Set Sample Rate [default=%default]")
    parser.add_option(
        "", "--spec", dest="spec", type="string", default='',
        help="Set Subdev [default=%default]")
    parser.add_option(
        "", "--stream-args", dest="stream_args", type="string", default='',
        help="Set Set additional stream args [default=%default]")
    parser.add_option(
        "", "--update-rate", dest="update_rate", type="eng_float", default=eng_notation.num_to_str(.1),
        help="Set Set GUI widget update rate [default=%default]")
    parser.add_option(
        "", "--wire-format", dest="wire_format", type="string", default='',
        help="Set Wire format [default=%default]")
    return parser


def main(top_block_cls=Testin, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(antenna=options.antenna, args=options.args, fft_size=options.fft_size, freq=options.freq, gain=options.gain, samp_rate=options.samp_rate, spec=options.spec, stream_args=options.stream_args, update_rate=options.update_rate, wire_format=options.wire_format)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
