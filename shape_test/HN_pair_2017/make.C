void make(int xxx=0){

  double Ltot = 35900.;
  int n_rebin = 50;

  TString channel = "MuMu";
  if(xxx==1) channel = "ElEl";

  TString channel2 = "DiMu";
  if(channel=="ElEl") channel2 = "DiEle";

  double error_bkgd = 0.30; // setting systematics for bkgs

  TFile *origin = new TFile("Bkg_VS_signal_cutbased_e.root");
  TFile *out = new TFile("shape_"+channel+".root","RECREATE");

  THStack *stack_background = (THStack *)origin->Get(channel+"/hs_h_OS_lljjjjmass_SR1_"+channel2);
  TH1D *background = (TH1D *)stack_background->GetStack()->Last();
  background->SetFillColor(0);
  background->SetLineColor(kBlack);
  background->SetName("background");
  cout <<"Bkgd : " << background->Integral() << endl;

  TH1D *background_up = (TH1D *)background->Clone();
  background_up->SetName("background_sh_normUp");
  background_up->Scale(1.+error_bkgd);

  TH1D *background_down = (TH1D *)background->Clone();
  background_down->SetName("background_sh_normDown");
  background_down->Scale(1-error_bkgd);

  //TH1D *data_obs = (TH1D *)origin->Get("hs_h_OS_lljjjjmass_SR1_DiMu");//FIXME
  TH1D *data_obs = (TH1D *)background->Clone(); //FIXME
  data_obs->SetMarkerStyle(24);
  data_obs->SetMarkerSize(1);
  data_obs->SetName("data_obs");
  cout << "Data : " << data_obs->Integral() << endl;

  //data_obs->Rebin(n_rebin);
  //background->Rebin(n_rebin);


  string elline;
  ifstream in("masses.txt");
  vector<TString> masses;
  while(getline(in,elline)){
    std::istringstream is( elline );
    TString mass;
    is >> mass;
    masses.push_back(mass);
  }
  
  cout << "1" << endl;

  out->cd();
  data_obs->Write();
  background->Write();
  background_up->Write();
  background_down->Write();
  
  cout << "2" << endl;


  for(unsigned int i=0; i<masses.size(); i++){

    TString mass = masses.at(i);

    TH1D *signal = (TH1D *)origin->Get(channel+"/h_OS_lljjjjmass_SR1_"+channel2+"_"+mass);
    TH1D *signal_den = (TH1D *)origin->Get(channel+"/Den_"+mass+"_h_OS_lljjjjmass_SR1_" + channel2);
    double eff = signal->Integral()/signal_den->GetBinContent(1);
    double scale = Ltot*eff/signal->Integral();

    //==== Scale signal by 1./1000. to increase r value.. now r is too small and can't find limit

    signal->Scale(scale*(1./1000.));
    signal->SetName("signal_"+mass);
    signal->SetLineWidth(3);
    signal->SetLineColor(kRed);
    cout << "Signal : " << signal->Integral() << "(eff = " << eff << ")" << endl;

    //signal->Rebin(n_rebin);

    //==== punzi
    double opt_obs(0.);
    double opt_bkgd(0.);
    double opt_sig(0.);
    double opt_punzi = -1;
    double opt_cut_left(0.), opt_cut_right(0.);
    for(int k=1; k<=background->GetXaxis()->GetNbins(); k++){
      for(int j=k+1; j<=background->GetXaxis()->GetNbins(); j++){
        double this_bkg = background->Integral(k,j);
        double this_eff = signal->Integral(k,j);
        //cout << i << "\t" << background->GetXaxis()->GetNbins() << " : " << this_bkg << "\t" << this_eff << endl;
        if(this_eff/(1.+sqrt(this_bkg)) > opt_punzi){
          opt_obs = data_obs->Integral(k,j);
          opt_bkgd = this_bkg;
          opt_sig = this_eff;
          opt_punzi = this_eff/(1.+sqrt(this_bkg));
          opt_cut_left = background->GetXaxis()->GetBinLowEdge(k);
          opt_cut_right = background->GetXaxis()->GetBinUpEdge(j);
        }
      }
    }

    out->cd();
    signal->Write();

    //==== up/down
    TH1D *signal_up = (TH1D *)signal->Clone();
    signal_up->SetName("signal_"+mass+"_sh_normUp");
    signal_up->Scale(1.+error_bkgd);
    signal_up->Write();

    TH1D *signal_down = (TH1D *)signal->Clone();
    signal_down->SetName("signal_"+mass+"_sh_normDown");
    signal_down->Scale(1-error_bkgd);
    signal_down->Write();

    cout << "["<<mass<<"]" << endl;
    cout << "opt_obs = " << opt_obs << endl;
    cout << "opt_bkgd = " << opt_bkgd << endl;
    cout << "opt_sig = " << opt_sig << endl;
    cout << "opt_cut_left = " << opt_cut_left << endl;
    cout << "opt_cut_right = " << opt_cut_right << endl;

    //==== shape card

    ofstream file_shape("./cards/shape_"+channel+"_"+mass+".txt", ios::trunc);
    file_shape << "imax 1" << endl;
    file_shape << "jmax 1" << endl;
    file_shape << "kmax *" << endl;
    file_shape << "---------------" << endl;

    file_shape << "shapes * * shape_"<<channel<< ".root $PROCESS $PROCESS_$SYSTEMATIC" << endl;
    file_shape << "---------------" << endl;
    file_shape << "bin 1" << endl;

    file_shape << "observation " << data_obs->Integral() << endl;
    //file_shape << "observation " << background->Integral() << endl;

    file_shape << "------------------------------" << endl;
    file_shape << "bin\t1\t1" << endl;
    file_shape << "process\t" << "signal_"+mass << "\tbackground" << endl;
    file_shape << "process\t0\t1" << endl;
    file_shape << "rate\t" << signal->Integral() << "\t" << background->Integral() << endl;
    file_shape << "--------------------------------" << endl;
    file_shape << "lumi\tlnN\t1.025\t1.025" << endl;
    file_shape << "norm\tlnN\t1.10\t" << 1.+error_bkgd << endl;
    file_shape << "sh_norm\tshapeN2\t1\t1" << endl;
    file_shape.close();

    //==== count card

    ofstream file_count("./cards/count_"+channel+"_"+mass+".txt", ios::trunc);
    file_count << "imax 1" << endl;
    file_count << "jmax 1" << endl;
    file_count << "kmax 2" << endl;
    file_count << "---------------" << endl;
    file_count << "bin 1" << endl;

    file_count << "observation " << opt_obs << endl;
    //file_count << "observation " << background->Integral() << endl;

    file_count << "------------------------------" << endl;
    file_count << "bin\t1\t1" << endl;
    file_count << "process\t" << "signal_"+mass << "\tbackground" << endl;
    file_count << "process\t0\t1" << endl;
    file_count << "rate\t" << opt_sig << "\t" << opt_bkgd << endl;
    file_count << "--------------------------------" << endl;
    file_count << "lumi\tlnN\t1.025\t1.025" << endl;
    file_count << "bgnorm\tlnN\t1.10\t" << 1.+error_bkgd << endl;
    file_count.close();


    //==== Write Shape Card

  }


  out->Close();
  

}
