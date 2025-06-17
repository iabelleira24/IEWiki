package iagoav.iewiki;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {
    private RecyclerView recyclerView;
    private RequestQueue queue;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        findViewById(R.id.btnTodosLosJugadores).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(MainActivity.this, CatalogoJugadoresActivity.class);
                startActivity(intent);
            }
        });

        recyclerView = findViewById(R.id.RecyclerV);
        queue = Volley.newRequestQueue(this);

        String url = "http://10.0.2.2:8000/equipos/";

        JsonObjectRequest request = new JsonObjectRequest(
                Request.Method.GET,
                url,
                null,
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        try {
                            JSONArray equiposnum = response.getJSONArray("equipos");
                            List<TeamDTO> equipos = new ArrayList<>();

                            for (int i = 0; i < equiposnum.length(); i++) {
                                JSONObject equipoObj = equiposnum.getJSONObject(i);
                                int id = equipoObj.getInt("id");
                                String nombre = equipoObj.getString("nombreE");
                                String entrenador = equipoObj.getString("entrenador");
                                String imagen = equipoObj.getString("imagen");



                                equipos.add(new TeamDTO(id, nombre, entrenador, imagen));
                            }

                            recyclerView.setLayoutManager(new LinearLayoutManager(MainActivity.this));
                            RecyclerViewAdapter adapter = new RecyclerViewAdapter(equipos);
                            recyclerView.setAdapter(adapter);

                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        error.printStackTrace();
                    }
                });

        queue.add(request);
    }
}
