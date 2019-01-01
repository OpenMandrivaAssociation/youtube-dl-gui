Summary:	GUI for youtube-dl
Name:		youtube-dl-gui
Version:	0.4
Release:	1
License:	Public Domain
Group:		Video
Url:		http://code.google.com/p/youtube-dlg/
# http://mrs0m30n3.github.io/youtube-dl-gui/
#Patch0:		youtube-dl-gui-0.3.5-icon.patch
Source0:	https://github.com/MrS0m30n3/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.png
BuildRequires:	imagemagick
BuildRequires:	python2-setuptools
BuildRequires:	wxPythonGTK
Requires:	ffmpeg
Requires:	wxPythonGTK
Requires:	youtube-dl
BuildArch:	noarch

%description
Youtube-dlG is a multi-platform GUI for the popular command line video
download tool youtube-dl. The GUI lets you download multiple videos at
once, can automatically convert downloaded videos to audio, lets you
select the video quality and more.

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/ytube.png
%{python_sitelib}/*

#----------------------------------------------------------------------------

%prep
%setup -q
#patch0 -p1

%build
python2 setup.py build

%install
python2 setup.py install --prefix=/usr --root=%{buildroot}

mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -s ../..%{python_sitelib}/youtube_dl_gui/__main__.py %{name}
chmod +x %{name}
popd

mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 0644 icons/ytube.png %{buildroot}%{_datadir}/pixmaps/ytube.png

mkdir -p  %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=YouTube-dl GUI
Comment=GUI for YouTube-dl
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Video;
EOF

for N in 16 32 48 64 128;
do
convert %{SOURCE1} -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %{buildroot}%{_iconsdir}/hicolor/${N}x${N}/apps/%{name}.png
done

