#############################################################################
# Generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#  Apr 08, 2021 09:56:02 PM CST  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Absolute
}




proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background #3f3f3f -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 398x222+532+258
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1061
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "pyHigher - 102Lab OCR Software"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    button $top.but47 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #acacac -disabledforeground #a3a3a3 \
        -font {-family {Microsoft YaHei UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground #ffffff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -pady 0 -text Stop 
    vTcl:DefineAlias "$top.but47" "StopButtom" vTcl:WidgetProc "Toplevel1" 1
    text $top.tex52 \
        -background #7f7f7f \
        -font {-family {Microsoft YaHei UI} -size 10 -weight bold} \
        -foreground #ffffff -height 152 -highlightbackground #ffffff \
        -highlightcolor black -insertbackground black -relief flat \
        -selectbackground blue -selectforeground #ffffff -width 259 \
        -wrap word 
    $top.tex52 configure -font "-family {Microsoft YaHei UI} -size 10 -weight bold"
    $top.tex52 insert end text
    vTcl:DefineAlias "$top.tex52" "Text" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $top.che54 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #3f3f3f \
        -font {-family {Microsoft YaHei UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground #ffffff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor #000000 -justify left -offrelief flat \
        -selectcolor #ffffff -text VO2 -variable VO2 
    vTcl:DefineAlias "$top.che54" "VO2Check" vTcl:WidgetProc "Toplevel1" 1
    vTcl:copy_lock $top.che54
    checkbutton $top.che59 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #3f3f3f -disabledforeground #a3a3a3 \
        -font {-family {Microsoft YaHei UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground #ffffff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -justify left -text VCO2 -variable VCO2 
    vTcl:DefineAlias "$top.che59" "VCO2Check" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $top.che60 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #3f3f3f -disabledforeground #a3a3a3 \
        -font {-family {Microsoft YaHei UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground #ffffff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -justify left -text VE -variable VE 
    vTcl:DefineAlias "$top.che60" "VECheck" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $top.che61 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #3f3f3f -disabledforeground #a3a3a3 \
        -font {-family {Microsoft YaHei UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground #ffffff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -justify left -text HR -variable HR 
    vTcl:DefineAlias "$top.che61" "HRCheck" vTcl:WidgetProc "Toplevel1" 1
    button $top.but62 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #acacac -disabledforeground #a3a3a3 \
        -font {-family {Microsoft YaHei UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground #ffffff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor #000000 -pady 0 -text Start 
    vTcl:DefineAlias "$top.but62" "StartButton" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $top.che47 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text Check -variable che47 
    vTcl:DefineAlias "$top.che47" "Checkbutton1" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but47 \
        -in $top -x 302 -y 140 -width 79 -relwidth 0 -height 58 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tex52 \
        -in $top -x 20 -y 50 -width 259 -relwidth 0 -height 152 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.che54 \
        -in $top -x 20 -y 10 -width 63 -relwidth 0 -height 27 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.che59 \
        -in $top -x 80 -y 10 -width 63 -relwidth 0 -height 27 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.che60 \
        -in $top -x 140 -y 10 -width 63 -relwidth 0 -height 27 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.che61 \
        -in $top -x 200 -y 10 -width 63 -relwidth 0 -height 27 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but62 \
        -in $top -x 300 -y 50 -width 79 -relwidth 0 -height 58 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.che47 \
        -in $top -x 260 -y 10 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}
