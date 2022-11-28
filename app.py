from flask import Flask, request, render_template
from calculator import Shell, ElepticBottom
from forms import ShellForm, BottomForm
app = Flask(__name__)
app.config.from_object('config')


@app.route('/shell', methods=['GET','POST'])
def shell():
    form = ShellForm()
    context = {'form': form, 'Sr': None, 'd0r': None, 
               'k_zap': None, 'title': "Расчет обечайки",
               'error': None}
 
    if form.validate_on_submit():
        sh = Shell()

        if form.S.data <= form.C.data:
            context['error'] = "S < C"
            return render_template('shell.html', **context)
 
        sh.set_P(float(form.P.data))
        sh.set_T(float(form.T.data))
        sh.set_Dvn(float(form.Dvn.data))
        sh.set_steel(form.steel.data)
        sh.set_S(float(form.S.data))
        sh.set_C(float(form.C.data))
        sh.set_phi(float(form.phi.data))
        Sr = sh.calculate_Sr()
        context['Sr'] = Sr
        context['d0r'] = sh.calculate_unreinforced_hole()
        context['k_zap'] = sh.calculate_k_zap()
    return render_template('shell.html', **context)
 
    
@app.route('/bottom', methods=['GET','POST'])
def bottom():
    form = BottomForm()
    context = {'form': form, 'Sr': None, 'd0r': None, 
               'k_zap': None, 'title': "Расчет обечайки",
               'error': None}
 
    if form.validate_on_submit():
        bt = ElepticBottom()
        bt.set_P(float(form.P.data))
        bt.set_T(float(form.T.data))
        bt.set_Dvn(float(form.Dvn.data))
        bt.set_steel(form.steel.data)
        bt.set_S(float(form.S.data))
        bt.set_C(float(form.C.data))
        bt.set_phi(float(form.phi.data))
        bt.set_H(float(form.H.data))
        Sr = bt.calculate_Sr()
        context['Sr'] = Sr
        context['d0r'] = bt.calculate_unreinforced_hole()
        context['k_zap'] = bt.calculate_k_zap()
    return render_template('shell.html', **context)

if __name__ == '__main__':
    app.run(debug=True)