%define fname            cedet
%define beta             pre4

%define cogre_evr        %{epoch}:0.5-%{release}
%define ede_evr          %{epoch}:1.0-0.pre4.%{release}
%define eieio_evr        %{epoch}:1.0-%{release}
%define semantic_evr     %{epoch}:2.0-0.pre4.%{release}
%define speedbar_evr     %{epoch}:1.0.1-%{release}

Name:           emacs-%{fname}
Version:        1.0
Release:        %mkrel 0.%{beta}.1
Epoch:          0
Summary:        Collection of Emacs Development Environment Tools
License:        GPL
URL:            http://sourceforge.net/projects/cedet/
Source:         http://download.sourceforge.net/sourceforge/cedet/%{fname}-%{version}%{beta}.tar.gz
Group:          Editors
Provides:       cedet = %{epoch}:%{version}-%{release}
Provides:       cogre = %{cogre_evr}
Provides:       emacs-cogre = %{cogre_evr}
Provides:       ede = %{ede_evr}
Provides:       emacs-ede = %{ede_evr}
Provides:       eieio = %{eieio_evr}
Obsoletes:      emacs-eieio < %{eieio_evr}
Provides:       emacs-eieio = %{eieio_evr}
Provides:       semantic = %{semantic_evr}
Obsoletes:      emacs-semantic < %{semantic_evr}
Provides:       emacs-semantic = %{semantic_evr}
Obsoletes:      emacs-speedbar < %{speedbar_evr}
Provides:       speedbar = %{speedbar_evr}
Provides:       emacs-speedbar = %{speedbar_evr}
Requires:       emacs-bin
BuildRequires:  emacs-bin
BuildRequires:  texinfo
BuildArch:      noarch

%description
CEDET is a collection of tools written with the end goal of
creating an advanced development environment in Emacs.

Emacs already is a great environment for writing software, but there
are additional areas that need improvement. Many new ideas for
integrated environments have been developed in newer products, such
as Microsoft's Visual environment, JBuilder, Eclipse, or KDevelop.
CEDET is a project which brings together several different tools
needed to implement advanced features.

CEDET tools including EIEIO, Semantic, Speedbar, EDE, and COGRE are
now distributed together in a single file. This simplifies
installation and version management.

%prep
%setup -q -n %{fname}-%{version}%{beta}
%{_bindir}/find . -type f -name "*.info" | %{_bindir}/xargs %{__rm}

%build
%{__make} clean-autoloads
%{__make} clean-all
%{__make}

%install
%{__rm} -rf %{buildroot}

# cedet-common
%{__mkdir_p} %{buildroot}%{_datadir}/emacs/site-lisp/cedet-common
%{__install} -m 644 common/*.el{,c} %{buildroot}%{_datadir}/emacs/site-lisp/cedet-common
%{__mkdir_p} %{buildroot}%{_datadir}/emacs/site-lisp/cedet-common/icons
%{__install} -m 644 common/icons/*.xpm %{buildroot}%{_datadir}/emacs/site-lisp/cedet-common/icons

# cedet-contrib
%{__mkdir_p} %{buildroot}%{_datadir}/emacs/site-lisp/cedet-contrib
%{__install} -m 644 contrib/*.el{,c} %{buildroot}%{_datadir}/emacs/site-lisp/cedet-contrib
%{__install} -m 644 contrib/*.wy %{buildroot}%{_datadir}/emacs/site-lisp/cedet-contrib

# cogre
%{__mkdir_p} %{buildroot}%{_datadir}/emacs/site-lisp/cogre
%{__install} -m 644 cogre/*.el{,c} %{buildroot}%{_datadir}/emacs/site-lisp/cogre
%{__install} -m 644 cogre/*.wy %{buildroot}%{_datadir}/emacs/site-lisp/cogre

# ede
%{__mkdir_p} %{buildroot}%{_datadir}/emacs/site-lisp/ede
%{__install} -m 644 ede/*.el{,c} %{buildroot}%{_datadir}/emacs/site-lisp/ede
#%{__rm} -f %{buildroot}%{_datadir}/emacs/site-lisp/ede/ede-proj-skel.el{,c}

# eieio
%{__mkdir_p} %{buildroot}%{_datadir}/emacs/site-lisp/eieio
%{__install} -m 644 eieio/*.el{,c} %{buildroot}%{_datadir}/emacs/site-lisp/eieio

# remove examples and tests
%{__rm} -f %{buildroot}%{_datadir}/emacs/site-lisp/eieio/tree.el{,c}
%{__rm} -f %{buildroot}%{_datadir}/emacs/site-lisp/eieio/call-tree.el{,c}
%{__rm} -f %{buildroot}%{_datadir}/emacs/site-lisp/eieio/linemark.el{,c}
%{__rm} -f %{buildroot}%{_datadir}/emacs/site-lisp/eieio/lmcompile.el{,c}
%{__rm} -f %{buildroot}%{_datadir}/emacs/site-lisp/eieio/eieio-tests.el{,c}

# semantic
%{__mkdir_p} %{buildroot}%{_datadir}/emacs/site-lisp/semantic
%{__install} -m 644 semantic/*.el{,c} %{buildroot}%{_datadir}/emacs/site-lisp/semantic
%{__install} -m 644 semantic/*.wy %{buildroot}%{_datadir}/emacs/site-lisp/semantic
%{__mkdir_p} %{buildroot}%{_datadir}/emacs/site-lisp/semantic/bovine
%{__install} -m 644 semantic/bovine/*.el{,c} %{buildroot}%{_datadir}/emacs/site-lisp/semantic/bovine
%{__install} -m 644 semantic/bovine/*.by %{buildroot}%{_datadir}/emacs/site-lisp/semantic/bovine
%{__mkdir_p} %{buildroot}%{_datadir}/emacs/site-lisp/semantic/wisent
%{__install} -m 644 semantic/wisent/*.el{,c} %{buildroot}%{_datadir}/emacs/site-lisp/semantic/wisent
%{__install} -m 644 semantic/wisent/*.wy %{buildroot}%{_datadir}/emacs/site-lisp/semantic/wisent

# speedbar
%{__mkdir_p} %{buildroot}%{_datadir}/emacs/site-lisp/speedbar
%{__install} -m 644 speedbar/*.el{,c} %{buildroot}%{_datadir}/emacs/site-lisp/speedbar
%{__install} -m 644 speedbar/*.xpm %{buildroot}%{_datadir}/emacs/site-lisp/speedbar

# Install symlinks for upstream compat
%{__mkdir_p} %{buildroot}%{_datadir}/emacs/site-lisp/cedet
pushd %{buildroot}%{_datadir}/emacs/site-lisp/cedet
%{__ln_s} ../cedet-common common
%{__ln_s} ../cedet-contrib contrib
%{__ln_s} ../cogre cogre
%{__ln_s} ../ede ede
%{__ln_s} ../eieio eieio
%{__ln_s} ../semantic semantic
%{__ln_s} ../speedbar speedbar
popd

# Install startup script
%{__mkdir_p} %{buildroot}%{_sysconfdir}/emacs/site-start.d
%{__cat} > %{buildroot}%{_sysconfdir}/emacs/site-start.d/cedet.el << EOF
;; Load CEDET
(load-file "%{_datadir}/emacs/site-lisp/cedet/common/cedet.el")

;; Enabling various SEMANTIC minor modes. See INSTALL.semantic for more ideas.
;; Select one of the following
(semantic-load-enable-code-helpers)
;; (semantic-load-enable-guady-code-helpers)
;; (semantic-load-enable-excessive-code-helpers)

;; Enable this if you develop in semantic, or develop grammars
;; (semantic-load-enable-semantic-debugging-helpers)
EOF

# Install infopages
%{__mkdir_p} %{buildroot}%{_infodir} 
for info in cogre/cogre.info \
         ede/ede.info \
         eieio/eieio.info \
         semantic/doc/bovine.info \
         semantic/doc/grammar-fw.info \
         semantic/doc/semantic-appdev.info \
         semantic/doc/semantic-langdev.info \
         semantic/doc/semantic-user.info \
         semantic/doc/semantic.info \
         semantic/doc/wisent.info \
         speedbar/speedbar.info; do
    %{__install} -m 644 ${info} %{buildroot}%{_infodir}
done

# Install docs
for dir in cogre common contrib ede eieio semantic speedbar; do
    for file in ChangeLog INSTALL NEWS ONEWS README; do
        if [ -f ${dir}/${file} ]; then
            %{__install} -m 644 ${dir}/${file} ${file}.${dir}
        fi
    done
done

%clean
%{__rm} -rf %{buildroot}

%post
%_install_info bovine.info
%_install_info cogre.info
%_install_info ede.info
%_install_info eieio.info
%_install_info grammar-fw.info
%_install_info semantic.info
%_install_info semantic-user.info
%_install_info semantic-appdev.info
%_install_info semantic-langdev.info
%_install_info speedbar.info
%_install_info wisent.info

%postun
%_remove_install_info bovine.info
%_remove_install_info cogre.info
%_remove_install_info ede.info
%_remove_install_info eieio.info
%_remove_install_info grammar-fw.info
%_remove_install_info semantic.info
%_remove_install_info semantic-user.info
%_remove_install_info semantic-appdev.info
%_remove_install_info semantic-langdev.info
%_remove_install_info speedbar.info
%_remove_install_info wisent.info

%files
%defattr(-, root, root)
%doc ChangeLog* INSTALL* *NEWS* PRERELEASE_CHECKLIST README* 
%{_datadir}/emacs/site-lisp/*
%config(noreplace) %{_sysconfdir}/emacs/site-start.d/*.el
%{_infodir}/*.info*
